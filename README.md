# AI Workflows with Streamlit

## English version

Run workflow easily with:

1. YAML file
2. openrouter.ai APIs
3. fabric-like patterns

### Web Interface

This project includes a Streamlit web interface that allows you to:
- Run workflows through a user-friendly web interface
- Configure API keys directly in the sidebar
- Upload text and process it with different workflows
- Download processed results

### Quick Start

#### Local Development
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure your API keys
4. Run the web app: `streamlit run app_web.py`

#### Streamlit Cloud Deployment
1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account and select this repository
4. Set `app_web.py` as the main file path
5. Configure secrets in Streamlit Cloud settings:
   - `OPENROUTER_API_KEY`
   - `EXA_API_KEY`
   - `OPENAI_API_KEY` (optional)
   - `OPENAI_API_BASE` (optional)

### Environment Variables

Create a `.env` file based on `.env.example` and configure:
- `OPENROUTER_API_KEY`: Your OpenRouter API key for LLM access
- `EXA_API_KEY`: Your EXA API key for search functionality
- `OPENAI_API_KEY`: Your OpenAI API key (optional)
- `OPENAI_API_BASE`: Custom OpenAI API base URL (optional)

For details, please look into [this article](https://wshuyi.medium.com/how-to-create-and-run-your-own-ai-workflows-with-ease-1a611e16d48f) for the basic operation and [this one](https://www.patreon.com/posts/how-to-use-line-110869551?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link) for advanced academic use.

## 中文说明（Chinese version）

有了这个简单的 Python 项目，你使用 AI 工作流，就不需要跟 fabric 的各种安装配置打交道了。

这个项目包含：
- 可以用 YAML 文件配置的 AI 工作流
- 在各个节点上，可以分别指定不同的 openrouter.ai API 调用大语言模型
- 所有 patterns 包含的结构化提示词，参考 fabric 写法，大多可以在两个项目之间兼容复用
- Streamlit 网页界面，方便部署和使用

### 网页界面

本项目包含 Streamlit 网页界面，提供以下功能：
- 通过用户友好的网页界面运行工作流
- 在侧边栏直接配置 API 密钥
- 上传文本并使用不同工作流处理
- 下载处理结果

### 快速开始

#### 本地开发
1. 克隆此仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 复制 `.env.example` 为 `.env` 并配置你的 API 密钥
4. 运行网页应用：`streamlit run app_web.py`

#### Streamlit Cloud 部署
1. 将此仓库 fork 到你的 GitHub 账户
2. 访问 [share.streamlit.io](https://share.streamlit.io)
3. 连接你的 GitHub 账户并选择此仓库
4. 设置 `app_web.py` 作为主文件路径
5. 在 Streamlit Cloud 设置中配置密钥：
   - `OPENROUTER_API_KEY`
   - `EXA_API_KEY`
   - `OPENAI_API_KEY`（可选）
   - `OPENAI_API_BASE`（可选）

基础操作请参考[这篇文章](https://mp.weixin.qq.com/s/tHIbczDuVfNdbmJlN6Xs9A)，进阶学术用途请参考[这篇文章](https://mp.weixin.qq.com/s/Xbfhh0w6-iNBpE7FExrRrA)

我为你录制了安装配置的视频教程，请[点击这个链接](https://www.bilibili.com/video/BV1Gs1GY5EUE/)。

注意我录制的视频教程是以 macOS 系统为例，后来又让学生帮我录制了 Windows 系统的安装过程演示，请[点击这个链接](https://www.bilibili.com/video/BV18vS8YNEdw/)查看。