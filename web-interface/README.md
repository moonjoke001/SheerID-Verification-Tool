# 🌐 SheerID Web 验证界面

## 快速启动

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 启动服务
```bash
python app.py
```

### 3. 访问界面
打开浏览器访问：http://localhost:5000

## 使用方法

1. 在输入框中粘贴 SheerID 验证链接
2. （可选）填入代理地址
3. 点击"开始验证"按钮
4. 等待验证完成，查看结果

## Docker 部署

```bash
docker build -t sheerid-web .
docker run -p 5000:5000 sheerid-web
```
