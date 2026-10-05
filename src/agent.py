from yolo_detector import YoloDetector
from llm_client import LLMClient

def main():
    detector = YoloDetector()
    llm = LLMClient()

    # 图片放在上级 images 文件夹
    img_file = "../images/desk.jpg"
    objects = detector.detect(img_file, threshold=0.5)

    print("==== 识别物品 ====")
    for item in objects:
        print(f"{item['name']}  置信度 {item['conf']:.2f}")

    item_text = "\n".join([f"- {x['name']}" for x in objects])
    prompt = f"""
你是一个专业的桌面整理助手。
用户会提供桌面上检测到的物品清单。

物品清单：
{item_text}

请根据物品给出：
1. 风险提示（比如水杯靠近电脑）
2. 分区摆放建议（学习区、生活区、杂物区）
3. 简短收纳技巧

分点输出，语气友好、实用，不要啰嗦。
"""
    print("\n==== 大模型回复 ====")
    reply = llm.ask(prompt)
    print(reply)

if __name__ == "__main__":
    main()