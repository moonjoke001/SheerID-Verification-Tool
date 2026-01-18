# 🐳 Docker 部署指南

## 快速开始

### 1. 构建镜像
```bash
cd /root/SheerID-Verification-Tool/one-verify-tool
docker build -t one-verify-tool .
```

### 2. 运行容器

**基础运行：**
```bash
docker run --rm one-verify-tool "https://services.sheerid.com/verify/xxx?verificationId=abc123"
```

**使用代理：**
```bash
docker run --rm one-verify-tool \
  "https://services.sheerid.com/verify/xxx?verificationId=abc123" \
  --proxy "http://user:pass@proxy.example.com:8080"
```

### 3. 使用 Docker Compose

**编辑 docker-compose.yml 修改 URL：**
```yaml
command: ["你的SheerID链接"]
```

**运行：**
```bash
docker-compose up
```

## 查看日志
```bash
docker logs one-verify
```

## 清理
```bash
docker-compose down
docker rmi one-verify-tool
```
