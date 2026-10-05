# 桌面整理智能助手

项目：YOLO 目标检测 + Ollama 本地大模型智能体

## 目录说明

- models 存放 YOLO 权重
- images 存放测试桌面照片
- src 源代码
  - yolo_detector.py YOLO 检测模块
  - llm_client.py Ollama 调用模块
  - agent.py 调度 Harness

## 运行方式

1. 启动 Ollama
2. 进入 src 目录
3. python agent.py

## 项目介绍

桌面整理智能助手，基于 YOLO 目标检测 + Ollama 本地大模型构建的智能体。

- 上传桌面照片，YOLO 识别桌面上所有物品
- 把识别出来的物品清单交给本地大模型
- 智能助手给出风险提示、分区摆放方案、收纳小技巧

## 环境要求

- Python 3.8 ~ 3.11
- ultralytics
- torch
- ollama

## 快速启动

1. 安装依赖

```bash
pip install ultralytics torch
```

2. 拉取本地大模型
```bash
ollama pull qwen2:7b
```

3. 切换到源代码目录

```bash
cd src
```

4. 运行桌面整理智能助手

```bash
python agent.py
```

## 架构说明

三层模块化设计

1. **YOLO 检测层 yolo_detector.py**：读取图片，识别桌面上物体，输出物品名称与置信度
2. **大模型层 llm_client.py**：封装 Ollama 接口，向本地大模型发送请求
3. **Harness 调度层 agent.py**：串联两个模块，拿到 YOLO 识别结果，组装提示词，调用大模型

## 演示示例

输入：一张包含电脑、水杯、书本的桌面图片

YOLO 识别输出：

- laptop 0.92
- cup 0.87
- book 0.76

大模型返回整理建议：

1. 风险提示：水杯靠近笔记本电脑，有泼洒进水风险，建议远离电脑 20 cm 以上。
2. 分区摆放建议：学习区放置笔记本电脑与书本，生活区单独摆放水杯。
3. 收纳技巧：书本竖直立放，减少桌面横向占用空间。


