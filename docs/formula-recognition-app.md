# 公式识别应用（Django + PaddlePaddle）

本目录下新增了一个可离线部署的 Django 示例项目，支持拖拽、粘贴、选择文件三种方式上传公式图片，并返回 LaTeX 与 Python 表达式。

## 快速启动
1. 安装依赖：`pip install -r requirements.txt`
2. 迁移数据库：`python manage.py migrate`
3. 运行开发服务器：`python manage.py runserver 0.0.0.0:8000`
4. 打开 <http://localhost:8000> 体验上传与识别。

> 默认启用 PaddleOCR，如需在无 Paddle 环境先行体验，可设置 `USE_DUMMY_RECOGNIZER=true` 启用内置假数据返回。

## 功能亮点
- **多种上传姿势**：拖拽、粘贴、文件选择，均支持多图批量识别。
- **结果展示**：美观卡片式布局，展示缩略图、置信度、时间，以及 LaTeX/Python 代码，带复制按钮。
- **离线友好**：通过环境变量切换真实 PaddleOCR 与内置示例输出，便于在离线或轻量环境先行验证流程。

## 目录结构
- `manage.py` / `formula_recognition/`：Django 项目配置
- `recognizer/`：上传与识别核心逻辑、模板、静态资源
- `requirements.txt`：运行依赖列表
