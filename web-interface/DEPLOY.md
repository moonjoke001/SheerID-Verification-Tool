# 🚀 部署到 Vercel

## 方法 1：通过 Vercel 网站（推荐）

### 步骤：

1. **访问 Vercel**
   - 打开 https://vercel.com
   - 使用 GitHub 账号登录

2. **导入项目**
   - 点击 "Add New" → "Project"
   - 选择你的 GitHub 仓库：`moonjoke001/SheerID-Verification-Tool`
   - Root Directory 设置为：`web-interface`

3. **配置项目**
   - Framework Preset: 选择 "Other"
   - Build Command: 留空
   - Output Directory: 留空
   - Install Command: `pip install -r requirements.txt`

4. **部署**
   - 点击 "Deploy"
   - 等待 1-2 分钟
   - 获得访问链接：`https://your-project.vercel.app`

## 方法 2：通过 Vercel CLI

### 步骤：

1. **安装 Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **登录**
   ```bash
   vercel login
   ```

3. **部署**
   ```bash
   cd /root/SheerID-Verification-Tool/web-interface
   vercel
   ```

4. **按提示操作**
   - Set up and deploy? Yes
   - Which scope? 选择你的账号
   - Link to existing project? No
   - Project name? 输入项目名
   - Directory? ./
   - Override settings? No

5. **生产部署**
   ```bash
   vercel --prod
   ```

## 自动部署

每次推送到 GitHub，Vercel 会自动重新部署。

## 访问地址

部署成功后，你会得到：
- 预览地址：`https://xxx-xxx.vercel.app`
- 生产地址：`https://your-project.vercel.app`

## 自定义域名（可选）

在 Vercel 项目设置中可以绑定自己的域名。
