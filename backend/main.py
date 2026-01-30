from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# 导入核心模块
from api import wecom, ai, customer, compliance
from core.database import init_db
from core.config import settings

# 初始化FastAPI应用
app = FastAPI(
    title="OpenDomain AI",
    description="轻量化、可扩展、合规化的AI+私域运营框架",
    version="0.1.0"
)

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化数据库
@app.on_event("startup")
async def startup_event():
    init_db()
    print("✅ OpenDomain AI 服务启动成功！")

# 注册路由
app.include_router(wecom.router, prefix="/api/wecom", tags=["企微API对接"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI核心能力"])
app.include_router(customer.router, prefix="/api/customer", tags=["客户管理"])
app.include_router(compliance.router, prefix="/api/compliance", tags=["合规管理"])

# 健康检查接口
@app.get("/health", tags=["健康检查"])
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
