# personaforge/persona.py
# 这个文件定义了 Persona 类，用来加载配置、抛彩蛋、对话，包含：
# - 根据用户输入的关键词动态调整彩蛋概率
# - 简单记忆（记住最近几句对话）
# - 支持“温柔模式”（配置中 mode: gentle 时彩蛋语气更温和）

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
        self.mode = self.config.get('mode', 'normal')   # 可选 gentle / normal

        # 简单记忆：用来存最近几轮对话
        self.short_term_memory = []     # 每个元素是 (角色, 内容)
        self.long_term_memory = []      # 预留，以后可以加

    def _maybe_egg(self, user_input):
        """
        根据用户输入，随机决定是否抛一颗彩蛋
        如果抛出，返回彩蛋文本；否则返回 None
        """
        if not self.wisdom_eggs:
            return None

        # 基础概率 5%
        prob = 0.05

        # 如果用户输入包含迷茫/困惑关键词，概率提升到 20%
        trigger_keywords = ["为什么", "怎么办", "迷茫", "不懂", "不知道", "困惑", "难过", "失败"]
        if any(k in user_input for k in trigger_keywords):
            prob = 0.20

        if random.random() < prob:
            egg = random.choice(self.wisdom_eggs)
            # 温柔模式下，给彩蛋加一个轻柔的前缀
            if self.mode == 'gentle':
                egg = f"（轻轻地说）{egg}"
            return egg
        return None

    def respond(self, user_input):
        """
        根据用户输入，生成回复
        user_input: 用户说的话（字符串）
        返回：AI 的回复（字符串）
        """
        # 1. 记录用户输入到短期记忆
        self.short_term_memory.append(("user", user_input))

        # 2. 先检查是否要抛彩蛋
        egg = self._maybe_egg(user_input)
        if egg:
            return egg

        # 3. 没有彩蛋时，生成普通回复
        #    如果记忆中有上一句用户的话，就引用一下，让对话更自然
        if len(self.short_term_memory) >= 2:
            last_user_msg = self.short_term_memory[-2][1]
            # 避免直接重复太长的句子，只截取前20字
            last_short = last_user_msg[:20] + "…" if len(last_user_msg) > 20 else last_user_msg
            return f"你刚才说“{last_short}”，让我再想想。"
        else:
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
