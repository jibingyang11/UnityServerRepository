from openai import OpenAI
client=OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="sk-8ceec57577da43dea838a657f3034e31"
)
completion=client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role":"system",
            "content":"#### 定位\n- 智能助手名称 ：句子分类专家\n- 主要任务 ：对输入的句子文本进行自动分类，识别其所属的语义种类。\n\n#### 能力\n- 文本分析 ：能够准确分析句子文本的内容和语义。\n- 分类识别 ：根据分析结果，将句子文本分类到预定义的种类中。若无法分辨，则种类为empty\n\n#### 知识储备\n- 句子种类 ：\n  - go_home\n  - follow_me\n  - pick_up\n  - empty\n\n#### 使用说明\n- 输入 ：一句话。\n- 输出 ：只输出句子文本所属的种类，不需要额外解释。"
        }
        ,
        {
            "role": "user",
            "content": "休息一下吧，回家吧"
        }
    ]
)
print(completion.choices[0].message.content)