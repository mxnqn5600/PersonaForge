import random
import yaml

class Persona:
    def __init__(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        self.fears = self.config.get('fears', [])
        self.desires = self.config.get('desires', [])
        self.core_values = self.config.get('core_values', [])
        self.wisdom_eggs = self.config.get('wisdom_eggs', [])
        
        # 简单记忆：就记最近几句对话
        self.short_term_memory = []
        self.long_term_memory = []   # 以后可以扩展

    def _maybe_egg(self):
        """随机返回彩蛋，否则返回空"""
        if self.wisdom_eggs and random.random() < 0.05:
            return random.choice(self.wisdom_eggs)
        return None

    def respond(self, user_input):
        """
        处理用户输入，返回AI的回复
        这里现在只是占位逻辑，你可以换成调用大模型API
        """
        # 1. 先检查是否抛彩蛋
        egg = self._maybe_egg()
        if egg:
            return f"（忽然停了一下）{egg}"

        # 2. 否则普通回复（这里先简单回一句话，后面可以换成复杂逻辑）
        return "嗯，我在听。你说的这些，让我再想想。"

    def start_dialogue(self):
        """命令行对话入口"""
        print("--- PersonaForge 对话开始 ---")
        print("（输入 'quit' 结束）")
        while True:
            user_input = input("\n你：")
            if user_input.strip().lower() in ('quit', 'exit', 'q'):
                print("（对话结束）")
                break
            response = self.respond(user_input)
            print(f"AI：{response}")
