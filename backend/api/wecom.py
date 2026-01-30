from fastapi import APIRouter, Body, Depends
import wecom_sdk
from core.config import settings
from core.compliance import check_sensitive_word
from api.customer import get_customer_by_wecom_id, create_customer

router = APIRouter()

# 获取企微SDK实例
def get_wecom_sdk():
    return wecom_sdk.WeComClient(
        corp_id=settings.wecom.corp_id,
        agent_id=settings.wecom.agent_id,
        secret=settings.wecom.secret,
        rate_limit=settings.wecom.api_rate_limit,
        retry_times=settings.wecom.retry_times
    )

# 企微消息接收接口
@router.post("/message/receive", summary="接收企微消息")
async def receive_wecom_message(
    message: dict = Body(...),
    wecom_client: wecom_sdk.WeComClient = Depends(get_wecom_sdk)
):
    try:
        # 解析企微消息
        msg_type = message.get("MsgType")
        wecom_user_id = message.get("FromUserName")
        content = message.get("Content", "").strip()
        
        # 1. 检查客户是否存在，不存在则创建
        customer = await get_customer_by_wecom_id(wecom_user_id)
        if not customer:
            # 获取客户基础信息（企微API）
            customer_info = wecom_client.get_user_info(wecom_user_id)
            await create_customer(
                wecom_user_id=wecom_user_id,
                wecom_name=customer_info.get("name", ""),
                phone=customer_info.get("mobile", "")
            )
        
        # 2. 合规检测：敏感词检查
        if settings.compliance.sensitive_word_check:
            is_sensitive, sensitive_words = check_sensitive_word(content)
            if is_sensitive:
                return {
                    "code": 400,
                    "msg": f"消息包含敏感词：{','.join(sensitive_words)}",
                    "data": None
                }
        
        # 3. 调用AI生成回答（后续对接ai/chat接口）
        # 此处简化，实际需调用ai/chat接口
        # ai_answer = await ai_chat(customer_id=wecom_user_id, question=content)
        
        # 4. 回复企微消息
        # wecom_client.send_message(wecom_user_id, ai_answer["data"]["answer"])
        
        return {
            "code": 200,
            "msg": "success",
            "data": None
        }
    except Exception as e:
        return {
            "code": 500,
            "msg": f"接收企微消息失败：{str(e)}",
            "data": None
        }
