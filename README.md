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
