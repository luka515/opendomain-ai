from fastapi import APIRouter, Body, Depends
from typing import List, Dict
from core.llm.base import load_llm
from core.config import settings
from core.redis import get_redis
from redis import Redis

router = APIRouter()

# 获取默认LLM实例
def get_llm():
    return load_llm(
        model_name=settings.llm.default_model,
        model_path=settings.llm.models[settings.llm.default_model]["path"],
        quantization=settings.llm.models[settings.llm.default_model]["quantization"]
    )

# AI对话接口
@router.post("/chat", summary="AI智能对话")
async def ai_chat(
    customer_id: str = Body(..., description="企微客户ID"),
    question: str = Body(..., description="用户问题"),
    llm: LLMBase = Depends(get_llm),
    redis: Redis = Depends(get_redis)
):
    try:
        # 从Redis获取对话历史
        history_key = f"chat_history:{customer_id}"
        history = await redis.get(history_key)
        history = eval(history) if history else []
        
        # 调用LLM生成回答
        answer = llm.invoke(question, history)
        
        # 合规处理：添加AI生成标注
        if settings.compliance.ai_content_label:
            answer = f"{answer}\n\n【AI生成内容，仅供参考】"
        
        # 更新对话历史
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})
        # 限制上下文长度
        if len(history) > settings.llm.context_window * 2:
            history = history[-settings.llm.context_window * 2:]
        await redis.set(history_key, str(history), ex=86400*7)  # 缓存7天
        
        return {
            "code": 200,
            "msg": "success",
            "data": {
                "answer": answer,
                "history": history
            }
        }
    except Exception as e:
        return {
            "code": 500,
            "msg": f"AI对话失败：{str(e)}",
            "data": None
        }

# RAG知识库问答接口
@router.post("/rag/chat", summary="知识库精准问答")
async def rag_chat(
    customer_id: str = Body(..., description="企微客户ID"),
    question: str = Body(..., description="用户问题"),
    kb_id: str = Body(default="default", description="知识库ID")
):
    # 后续实现RAG逻辑（Chroma向量库检索+LLM生成）
    pass
