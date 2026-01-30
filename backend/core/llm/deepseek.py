from transformers import AutoModelForCausalLM, AutoTokenizer
from .base import LLMBase, register_llm
from typing import Dict, List

@register_llm("deepseek")
class DeepSeekLLM(LLMBase):
    def _load_model(self):
        """加载DeepSeek模型"""
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
        # 量化加载（适配低显存）
        if self.quantization == "INT4":
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                trust_remote_code=True,
                load_in_4bit=True,
                device_map="auto"
            )
        elif self.quantization == "INT8":
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                trust_remote_code=True,
                load_in_8bit=True,
                device_map="auto"
            )
        else:
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                trust_remote_code=True,
                device_map="auto"
            )

    def invoke(self, prompt: str, history: List[Dict] = None) -> str:
        """调用DeepSeek模型"""
        # 拼接对话历史
        input_text = prompt
        if history:
            history_text = "\n".join([f"{h['role']}: {h['content']}" for h in history])
            input_text = f"{history_text}\nuser: {prompt}\nassistant:"
        
        # 生成回答
        inputs = self.tokenizer(input_text, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=2048,
            temperature=0.7,
            do_sample=True
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # 提取assistant回答
        assistant_answer = response.split("assistant:")[-1].strip()
        return assistant_answer
