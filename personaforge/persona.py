# personaforge/persona.py
# 这个文件定义了 Persona 类，用来加载配置、抛彩蛋、对话

import random
import yaml

class Persona:
    def __init__(self, config_path):
        """
        初始化人格
        config_path: 配置文件路径，比如 "config/persona_core.yaml"
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

            # 从配置里取出各项（如果没有就设为空列表）
            self.fears = self.config.get('fears', [])
            self.desires = self.config.get('desires', [])
            self.core_values = self.config.get('core_values', [])
            self.wisdom_eggs = self.config.get('wisdom_eggs', [])

            # 简单记忆：用来存最近几轮对话（以后可以扩展）
            self.short_term_memory = []
            self.long_term_memory = []

    def _maybe_egg(self):
        """
        内部方法：随机决定是否抛一颗彩蛋
        如果抛出，返回彩蛋文本；否则返回 None
        """
        if not self.wisdom_eggs:
            return None
        if random.random() < 0.05:
            return random.choice(self.wisdom_eggs)
            return None

    def respond(self, user_input):
        """
        根据用户输入，生成回复
        user_input: 用户说的话（字符串）
        返回：AI 的回复（字符串）
        """
        # 1. 先检查是否要抛彩蛋
        egg = self._maybe_egg()
        if egg:
            return f"（忽然停了一下）{egg}"

            # 2. 没有彩蛋时，做一个简单回复（以后可以换成调用大模型）
            return "嗯，我在听。你说的这些，让我再想想。"

    def start_dialogue(self):
        """
        启动命令行对话
        """
        print("--- PersonaForge 对话开始 ---")
        print("（输入 'quit' 或 'exit' 或 'q' 结束）")
        while True:
            user_input = input("\n你：")
            if user_input.strip().lower() in ('quit', 'exit', 'q'):
                print("（对话结束）")
                break
            response = self.respond(user_input)
            print(f"AI：{response}")
