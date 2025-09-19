import streamlit as st
import subprocess
import tempfile
import os
from dotenv import load_dotenv
import yaml

# Load environment variables
load_dotenv()

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

def create_api_key_input(key_name, env_var_name):
    """创建API key输入框，只在session_state中临时存储"""
    # 初始化session state
    session_key = f"api_key_{env_var_name.lower()}"
    if session_key not in st.session_state:
        st.session_state[session_key] = ""
    
    # 创建密码输入框
    api_key = st.text_input(
        f"{key_name} API Key", 
        value=st.session_state[session_key],
        type="password",
        help=f"Enter your {key_name} API key (只在当前会话中有效，退出后自动清除)",
        key=f"input_{session_key}"
    )
    
    # 更新session state和环境变量
    if api_key:
        st.session_state[session_key] = api_key
        os.environ[env_var_name] = api_key
    else:
        # 如果清空了输入框，也清空环境变量
        if env_var_name in os.environ:
            del os.environ[env_var_name]
    
    return api_key

def load_workflows():
    workflows = []
    config_dir = os.path.join(current_dir, 'config')
    for file in os.listdir(config_dir):
        if file.endswith('.yaml'):
            workflows.append(file.replace('.yaml', ''))
    return workflows

def load_config(workflow):
    config_path = os.path.join(current_dir, 'config', f'{workflow}.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Streamlit app
st.title('Text Processing Workflow')

# API Keys section in sidebar
with st.sidebar:
    st.header('🔐 API Keys')
    st.info("🛡️ 安全提醒：API 密钥只在当前会话中临时存储，浏览器关闭后自动清除，不会保存到服务器")
    
    openrouter_api_key = create_api_key_input("OpenRouter", "OPENROUTER_API_KEY")
    exa_api_key = create_api_key_input("EXA", "EXA_API_KEY")
    
    # 添加OpenAI设置
    st.subheader('OpenAI Settings')
    openai_api_key = create_api_key_input("OpenAI", "OPENAI_API_KEY")
    
    # OpenAI API Base URL - 也只在session中存储
    if "api_key_openai_api_base" not in st.session_state:
        st.session_state["api_key_openai_api_base"] = ""
    
    openai_api_base = st.text_input(
        "OpenAI API Base URL",
        value=st.session_state["api_key_openai_api_base"],
        help="Enter your OpenAI API base URL (optional, 只在当前会话中有效)",
        key="input_openai_api_base"
    )
    
    # 更新session state和环境变量
    if openai_api_base:
        st.session_state["api_key_openai_api_base"] = openai_api_base
        os.environ["OPENAI_API_BASE"] = openai_api_base
    else:
        if "OPENAI_API_BASE" in os.environ:
            del os.environ["OPENAI_API_BASE"]
    
    # 添加清除所有API密钥的按钮
    st.divider()
    if st.button("🗑️ 清除所有 API 密钥", type="secondary", use_container_width=True):
        # 清除session state
        keys_to_clear = [
            "api_key_openrouter_api_key",
            "api_key_exa_api_key", 
            "api_key_openai_api_key",
            "api_key_openai_api_base"
        ]
        for key in keys_to_clear:
            if key in st.session_state:
                st.session_state[key] = ""
        
        # 清除环境变量
        env_vars_to_clear = ["OPENROUTER_API_KEY", "EXA_API_KEY", "OPENAI_API_KEY", "OPENAI_API_BASE"]
        for var in env_vars_to_clear:
            if var in os.environ:
                del os.environ[var]
        
        st.success("✅ 所有 API 密钥已清除")
        st.rerun()
    
    # 显示当前API密钥状态
    st.divider()
    st.subheader("🔍 当前状态")
    status_info = []
    if st.session_state.get("api_key_openrouter_api_key"):
        status_info.append("✅ OpenRouter API Key")
    else:
        status_info.append("❌ OpenRouter API Key")
        
    if st.session_state.get("api_key_exa_api_key"):
        status_info.append("✅ EXA API Key")
    else:
        status_info.append("❌ EXA API Key")
        
    if st.session_state.get("api_key_openai_api_key"):
        status_info.append("✅ OpenAI API Key")
    else:
        status_info.append("❌ OpenAI API Key")
        
    if st.session_state.get("api_key_openai_api_base"):
        status_info.append("✅ OpenAI API Base")
    else:
        status_info.append("❌ OpenAI API Base")
    
    for info in status_info:
        st.text(info)

# Workflow selection
workflows = load_workflows()
selected_workflow = st.selectbox('Select Workflow', workflows)

# Load config for selected workflow
config = load_config(selected_workflow)

# Text input
input_text = st.text_area('Enter text to process')

# Process button
if st.button('Process'):
    if input_text:
        # Save input text to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
            temp_file.write(input_text)
            temp_file_path = temp_file.name

        # Prepare command with full path to app.py
        app_path = os.path.join(current_dir, 'app.py')
        cmd = ['python', app_path, temp_file_path, '--workflow', selected_workflow]

        # Run the command
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Display output and provide download link
            output_file = os.path.join(os.path.dirname(temp_file_path), f'{selected_workflow}-output.md')
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    output_content = f.read()
                st.text_area('Output', output_content, height=300)
                st.download_button('Download Output', output_content, file_name=f'{selected_workflow}-output.md')
            else:
                st.warning('Output file not found. Displaying standard output and error for debugging:')
                st.text_area('Standard Output', result.stdout, height=300)
                if result.stderr:
                    st.text_area('Standard Error', result.stderr, height=300)

        except subprocess.CalledProcessError as e:
            st.error(f'Error occurred. Displaying standard output and error for debugging:')
            st.text_area('Standard Output', e.stdout, height=300)
            st.text_area('Standard Error', e.stderr, height=300)

        finally:
            # Clean up temporary file
            os.unlink(temp_file_path)
    else:
        st.warning('Please enter some text to process.')
