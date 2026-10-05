```markdown
# 工程开发日志

## 2026-10-04
- 学习 ultralytics 库，完成 YOLO 图片目标检测
- 成功识别图片中的物体
- 遇到问题：YOLO 首次运行自动下载权重，下载速度很慢
- 解决办法：手动下载 yolov8n.pt 放到 models 文件夹

## 2026-10-05
- 项目模块化拆分，拆成 yolo_detector、llm_client、agent
- 接入 Ollama 本地大模型
- 遇到问题：Python 缩进报错 IndentationError
- 解决办法：重新粘贴缩进对齐的完整代码

## 2026-10-06
- 给智能体编写桌面整理助手的提示词
- 准备 3 份测试图片 clean.jpg、messy.jpg、cup_desk.jpg
- 分别测试 3 种桌面场景，验证大模型输出整理方案
