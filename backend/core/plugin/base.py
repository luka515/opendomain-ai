from abc import ABC, abstractmethod
from typing import Dict, Any

class PluginBase(ABC):
    """插件基类，统一插件接口"""
    def __init__(self, plugin_name: str, version: str, description: str):
        self.plugin_name = plugin_name
        self.version = version
        self.description = description
        self.enabled = True

    @abstractmethod
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """插件执行逻辑（子类实现）
        :param data: 输入数据（按需定义）
        :return: 执行结果
        """
        pass

    def enable(self):
        """启用插件"""
        self.enabled = True

    def disable(self):
        """禁用插件"""
        self.enabled = False

# 插件注册器
PLUGIN_REGISTRY = {}
def register_plugin(plugin_name: str):
    def decorator(cls):
        PLUGIN_REGISTRY[plugin_name] = cls
        return cls
    return decorator

# 加载插件
def load_plugin(plugin_name: str) -> PluginBase:
    if plugin_name not in PLUGIN_REGISTRY:
        raise ValueError(f"插件不存在：{plugin_name}")
    return PLUGIN_REGISTRY[plugin_name]()
