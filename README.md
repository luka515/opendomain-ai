# OpenDomain AI
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/{luka515}/opendomain-ai.svg?style=social)](https://github.com/{luka515}/opendomain-ai)
[![GitHub Forks](https://img.shields.io/github/forks/{luka515}/opendomain-ai.svg?style=social)](https://github.com/{luka515}/opendomain-ai)

### 一款**轻量化、可扩展、合规化**的开源AI+私域运营框架
聚焦「企微私域+大模型AI」核心场景，为中小团队/开发者提供低门槛的AI私域工具开发底座，实现**技术普惠、社区共建**。

## 🚀 快速开始
### 环境要求
- Docker + Docker Compose
- 8G以上内存（GPU可选，推荐16G+）
- 企微开放平台账号（获取CorpID/AgentID/Secret）

### 部署步骤
1. 克隆代码
```bash
git clone https://github.com/{luka515}/opendomain-ai.git
cd opendomain-ai

2.配置环境变量
修改.env文件，替换企微 API 密钥、模型路径等配置：
cp .env.example .env  # 如有example文件，否则直接编辑.env

3.准备大模型文件
将 DeepSeek/Qwen 模型文件放入./models目录（推荐 DeepSeek-llm-7b-chat 轻量化版本）

4.启动服务
chmod +x ./scripts/deploy.sh
./scripts/deploy.sh start

5.验证服务
后端接口文档：http://localhost:8000/docs
健康检查：http://localhost:8000/health

🏗️ 项目架构（MVP 版）
企微用户

企微开放API

OpenDomain AI 后端
Python+FastAPI

AI核心层
DeepSeek+LangChain

数据层
PostgreSQL+Redis

前端管理后台
Vue3+Element Plus

开发者

二次开发/插件开发

📚 核心功能
1. AI 智能对话
支持 DeepSeek/Qwen/ChatGLM 开源大模型
对话历史缓存（Redis），支持上下文管理
AI 生成内容自动标注，符合合规要求
2. 企微合规对接
企微 API 限流 / 重试机制
敏感词检测，数据脱敏存储
操作审计日志，支持导出
3. 插件化扩展
自定义插件开发规范
内置客户标签、合规检测、内容生成插件

🔧 二次开发指南
插件开发
继承PluginBase基类，实现execute方法
使用@register_plugin装饰器注册插件
将插件放入./plugins目录，重启服务即可加载
模型扩展
继承LLMBase基类，实现_load_model和invoke方法
使用@register_llm装饰器注册模型
在config.yaml中配置新模型路径和参数

🤝 社区共建
提交 PR：请遵循贡献指南
提交 Issue：使用Issue 模板
交流群：待补充
