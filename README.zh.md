# Skill Prompt

> 将你的大白话需求，一键锻造成高纯度的 AI Agent 技能提示词。

**[English Docs](./README.md)**

---

## 功能特性

- **一键生成** — 用大白话描述需求，自动生成结构化的 Skill 系统提示词
- **多模型支持** — DeepSeek-R1、GPT-4o、GPT-4o-mini 或任意兼容 OpenAI 的自定义 API
- **中英双语** — 完整的中文 / 英文界面切换
- **深色 / 浅色 / 跟随系统主题** — 支持自定义背景图片
- **打字动画** — 10 条示例需求循环展示
- **停止生成** — 随时取消正在生成的请求
- **Docker 就绪** — 一条命令部署

---

## 快速开始

### 前置条件

- Python 3.11+
- Docker（可选）

### 本地运行

```bash
# 安装依赖
pip install -r backend/requirements.txt

# 启动服务
cd backend
python main.py
```

在浏览器中打开 `http://localhost:8000`。

### Docker 部署

```bash
docker compose up -d --build
```

在浏览器中打开 `http://你的服务器IP:7619`。

---

## 项目结构

```
mimo-skill-factory/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── README.md
├── README.zh.md
├── backend/
│   ├── main.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    └── assets/
        └── favicon.png
```

---

## 工作原理

1. 用大白话描述一个 Skill 需求
2. 应用将需求连同结构化元提示词一起发送给 AI 模型
3. 模型返回一段严密结构化的 Skill 系统提示词
4. 复制结果，在你的本地 AI Agent 中使用

---

## 配置说明

所有设置保存在浏览器的 `localStorage` 中：

| 设置项 | 说明 |
|---|---|
| API Key | 你的 AI 模型密钥（不会上传） |
| Base URL | API 接口地址 |
| Model Name | 模型名称 |
| 主题 | 深色 / 浅色 / 跟随系统 |
| 语言 | 中文 / English |
| 背景 | 自定义背景图片链接或上传 |

---

## API 接口

```
POST /api/generate-prompt
Content-Type: application/json

{
  "requirement": "你的技能描述",
  "config": {
    "provider": "deepseek-r1",
    "api_key": "sk-xxx",
    "base_url": "https://api.deepseek.com",
    "model_name": "deepseek-reasoner"
  },
  "lang": "zh"
}
```

返回：

```json
{
  "success": true,
  "prompt": "# 角色与目标\n..."
}
```

---

## 技术栈

- **后端**：Python、FastAPI、OpenAI SDK
- **前端**：原生 HTML / CSS / JS
- **部署**：Docker

---

## 开源协议

MIT
