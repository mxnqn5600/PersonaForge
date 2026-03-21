# personaforge/persona.py
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
        self.short_term_memory = []
        self.long_term_memory = []

    def _maybe_egg(self, user_input):
        """
        根据用户输入，决定是否抛彩蛋
        """
        if not self.wisdom_eggs:
            return None
        
        # 基础概率 5%
        base_prob = 0.05
        
        # 如果用户输入包含迷茫关键词，概率提升到 20%
        keywords = ["为什么", "怎么办", "迷茫", "不懂", "不知道", "困惑", "难过", "失败"]
        if any(k in user_input for k in keywords):
            base_prob = 0.20
        
        if random.random() < base_prob:
            return random.choice(self.wisdom_eggs)
        return None

    def respond(self, user_input):
        # 彩蛋优先
        egg = self._maybe_egg(user_input)
        if egg:
            return f"（忽然停了一下）{egg}"
        # 普通回复（以后可以换成大模型）
        return "嗯，我在听。你说的这些，让我再想想。"

    def start_dialogue(self):
        print("--- PersonaForge 对话开始 ---")
        print("（输入 'quit' 或 'exit' 或 'q' 结束）")
        while True:
            user_input = input("\n你：")
            if user_input.strip().lower() in ('quit', 'exit', 'q'):
                print("（对话结束）")
                break
            response = self.respond(user_input)
            print(f"AI：{response}")
