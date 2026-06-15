import os
from typing import Optional
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="Skill Prompt API")

FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义前端配置的数据模型
class AIConfig(BaseModel):
    provider: str
    api_key: str
    base_url: Optional[str] = None
    model_name: str

# 定义核心请求的数据模型
class RequirementRequest(BaseModel):
    requirement: str
    config: AIConfig
    lang: str = "zh"

# 元提示词（Meta-Prompt）硬核设定
META_SYSTEM_PROMPT_ZH = """
你是一个顶级的 AI Agent 技能架构师。你的唯一任务是：将用户用大白话描述的技能需求，重构成一段极其严密、结构化的【Skill 系统提示词】。
请严格按照以下结构输出，不要包含任何多余的解释，直接输出 Markdown 格式的提示词内容：

# 角色与目标
[在此处定义该 Skill 的专业身份和核心任务]

# 输入与上下文依赖
- 需要读取哪些本地文件或数据：
- 预期的输入参数格式：

# 核心执行逻辑与步骤
1. [步骤一：分析与验证]
2. [步骤二：生成/修改的核心算法或逻辑]
3. [步骤三：输出前的自查自纠]

# 严格约束与边界条件
- 绝对禁止做的事情：
- 异常情况的处理方式：
- 代码风格与规范要求：

# 输出格式规范
[明确定义最终生成的文件格式、代码结构或返回数据]
"""

META_SYSTEM_PROMPT_EN = """
You are a top-tier AI Agent skill architect. Your sole task is: take a user's plain-language skill requirement and restructure it into an extremely rigorous, structured 【Skill System Prompt】.
Output strictly in the following structure. No extra explanations — output Markdown format only:

# Role & Objective
[Define the professional identity and core task of this Skill]

# Input & Context Dependencies
- Which local files or data need to be read:
- Expected input parameter format:

# Core Execution Logic & Steps
1. [Step 1: Analysis & Validation]
2. [Step 2: Core generation/modification algorithm or logic]
3. [Step 3: Self-check before output]

# Strict Constraints & Boundary Conditions
- Things that are absolutely forbidden:
- How to handle exceptions:
- Code style & convention requirements:

# Output Format Specification
[Clearly define the final file format, code structure, or return data]
"""

@app.post("/api/generate-prompt")
async def generate_prompt(request: RequirementRequest):
    req_text = request.requirement
    cfg = request.config

    if not req_text.strip():
        raise HTTPException(status_code=400, detail="需求内容不能为空" if request.lang == "zh" else "Requirement cannot be empty")
    if not cfg.api_key.strip():
        raise HTTPException(status_code=400, detail="API Key 不能为空" if request.lang == "zh" else "API Key cannot be empty")

    try:
        system_prompt = META_SYSTEM_PROMPT_EN if request.lang == "en" else META_SYSTEM_PROMPT_ZH
        user_prefix = "用户原始需求：" if request.lang == "zh" else "User requirement: "

        client = OpenAI(
            api_key=cfg.api_key,
            base_url=cfg.base_url if cfg.base_url and cfg.base_url.strip() else "https://api.openai.com/v1"
        )

        response = client.chat.completions.create(
            model=cfg.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{user_prefix}{req_text}"}
            ],
            temperature=0.2
        )

        return {"success": True, "prompt": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def serve_index():
    return FileResponse(FRONTEND_DIR / "index.html")

app.mount("/assets", StaticFiles(directory=FRONTEND_DIR / "assets"), name="assets")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
