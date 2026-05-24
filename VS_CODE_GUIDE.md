# 📖 VS Code Complete Operating Guide

## 🎯 Goal

Complete the following 5 steps in VS Code:
1. ✅ Open project
2. ✅ Read START_HERE.md
3. ✅ Configure API Key
4. ✅ Start system
5. ✅ Upload thesis

---

## 🚀 Step 1: Open Project in VS Code

### Method A: Command Line (Fastest)

```bash
# Run in terminal (any location)
code /Users/siyuzhang/Desktop/KM/paper-analyzer
```

### Method B: VS Code Interface

1. Click **File** → **Open Folder**
2. Navigate to `/Users/siyuzhang/Desktop/KM/paper-analyzer`
3. Click **Open**

---

## 📖 第2步：在VS Code中阅读START_HERE.md

### 打开文件

左侧资源管理器中找到 `START_HERE.md`，点击打开

或快捷键：
```
Cmd + O  (打开文件)
输入: START_HERE
Enter
```

### 预览模式

- VS Code会以Markdown预览形式显示
- 点击右上角 **Open Preview to the Side** (分屏预览)
- 左侧是源码，右侧是渲染效果

---

## 🔑 第3步：配置API Key（详细步骤）

### 3.1 打开.env文件

**方法1：左侧资源管理器**
```
1. 看VS Code左侧文件列表
2. 找到 .env 文件
3. 点击打开
```

**方法2：快捷键**
```
Cmd + P  (打开快速搜索)
输入: .env
选择: .env
```

**方法3：直接打开**
```
Cmd + Shift + P  (命令面板)
输入: open file
选择: /Users/siyuzhang/Desktop/KM/paper-analyzer/.env
```

### 3.2 查看.env文件的内容

```
当前内容看起来像这样：
ANTHROPIC_API_KEY=your_api_key_here
DEBUG=True
PORT=8000
MAX_FILE_SIZE=50000000
```

### 3.3 获取Claude API Key

**完整流程（3分钟）：**

```
1️⃣ 打开浏览器
   访问: https://console.anthropic.com/

2️⃣ 如果没有账户，点击 "Sign Up"
   输入: 邮箱和密码
   点击: Create Account
   
3️⃣ 验证邮箱
   Anthropic会发送验证邮件
   点击邮件中的链接

4️⃣ 登录到控制台
   https://console.anthropic.com/

5️⃣ 导航到API Keys
   左侧菜单 → API Keys

6️⃣ 创建新密钥
   点击: "Create Key" 按钮
   
7️⃣ 复制密钥
   你会看到一个长字符串: sk-ant-xxxxxxxxxxxxxxxxxxxx
   点击"Copy"复制到剪贴板
   
⚠️  重要: 这是你唯一看到完整密钥的机会！
   不要丢失，妥善保管
```

### 3.4 粘贴API Key到.env文件

在VS Code中：

```
1. 找到 ANTHROPIC_API_KEY=your_api_key_here 这一行

2. 删除 your_api_key_here 部分

3. 粘贴你的密钥
   结果看起来像:
   ANTHROPIC_API_KEY=sk-ant-j2x9k2x9k2x9k2x9k2x9k2x9k

4. 保存文件
   按 Cmd + S
   
   或 File → Save
```

### 3.5 验证配置

```bash
# 打开VS Code集成终端 (Cmd + `)
# 运行以下命令验证配置

python3 -c "from backend.config import config; print(f'API Key configured: {bool(config.ANTHROPIC_API_KEY)}')"

# 应该输出: API Key configured: True
```

---

## 🚀 第4步：启动系统（在VS Code中）

### 4.1 打开集成终端

**方法1：快捷键**
```
Ctrl + `  (这是反引号键)
```

**方法2：菜单**
```
点击 Terminal → New Terminal
```

### 4.2 确认终端位置

```bash
# 终端应该显示
/Users/siyuzhang/Desktop/KM/paper-analyzer

# 如果不对，运行
cd /Users/siyuzhang/Desktop/KM/paper-analyzer
```

### 4.3 激活虚拟环境

```bash
# 运行
source venv/bin/activate

# 你应该看到终端前面出现 (venv) 标志
# 表示虚拟环境已激活
```

### 4.4 启动系统

```bash
# 运行启动脚本
./start.sh

# 或手动启动
# cd backend
# python -m uvicorn main:app --reload
```

### 4.5 看到这个输出就表示成功！

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Reload enabled
```

**不要关闭这个终端！** ⚠️ 保持运行

---

## 📱 第5步：上传论文进行分析

### 方法1️⃣：Web界面（推荐，最简单）

#### 5.1 打开前端页面

**在浏览器地址栏输入：**
```
file:///Users/siyuzhang/Desktop/KM/paper-analyzer/frontend/index.html
```

或者：
```bash
# 在VS Code中新打开一个终端 (Cmd + `)
# 运行
open /Users/siyuzhang/Desktop/KM/paper-analyzer/frontend/index.html
```

#### 5.2 看到的界面

```
┌─────────────────────────────────────┐
│   论文智能评估系统                   │
│                                      │
│   [点击或拖拽上传PDF论文]             │
│   支持PDF格式，最大50MB              │
│                                      │
│   [开始分析]  [清除文件]              │
└─────────────────────────────────────┘
```

#### 5.3 上传论文文件

**方法A：拖拽上传（最简单）**
```
1. 在文件管理器中找到你的PDF论文
2. 拖拽到Web界面的上传区域
3. 自动开始上传
```

**方法B：点击上传**
```
1. 点击上传区域
2. 选择PDF文件
3. 点击打开
```

#### 5.4 等待分析

```
✓ 文件上传中...
✓ 正在分析论文... (1-2分钟)
✓ 生成报告...

你会看到：
- 总体评分 (0-100)
- 6个维度的评分
- 专业建议
- 格式检查结果
- 论文结构分析
```

### 方法2️⃣：API文档界面

#### 5.1 打开API文档

```
在浏览器中访问：
http://localhost:8000/docs
```

#### 5.2 找到上传端点

```
找到 POST /upload
点击它展开详情
```

#### 5.3 上传文件

```
1. 点击 "Try it out"
2. 点击 "Choose file" 选择PDF
3. 点击 "Execute" 执行
4. 等待响应
```

### 方法3️⃣：命令行方式

**打开新的VS Code终端（不要关闭start.sh的终端）：**

```bash
# 新终端中运行
cd /Users/siyuzhang/Desktop/KM/paper-analyzer
source venv/bin/activate

# 假设论文在桌面
python3 demo_client.py --analyze ~/Desktop/my_paper.pdf

# 你会看到详细的分析结果
```

---

## 📊 完整工作流程（从开始到完成）

### 时间轴：30分钟内完成

```
0:00 - 打开VS Code
      code /Users/siyuzhang/Desktop/KM/paper-analyzer

0:05 - 阅读START_HERE.md
      （快速浏览，了解大概）

0:10 - 获取API Key
      访问 https://console.anthropic.com/
     （需要5分钟）

0:15 - 配置.env文件
      编辑 ANTHROPIC_API_KEY 一行

0:20 - 启动系统
      ./start.sh
      等待看到 "Uvicorn running on..."

0:25 - 打开Web界面
      file:///.../frontend/index.html

0:30 - 上传第一篇论文
      拖拽PDF到界面
      等待分析完成（1-2分钟）

0:35 - 查看结果 ✅
```

---

## ⚠️ 常见问题快速解决

### Q1: 启动脚本失败了

**症状**: 运行 `./start.sh` 出错

**解决**:
```bash
# 确保虚拟环境激活
source venv/bin/activate

# 手动启动
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

### Q2: API Key不生效

**症状**: 分析时提示API Key错误

**检查**:
```bash
# 1. 验证.env文件已保存 (Cmd+S)
# 2. 检查API Key格式: sk-ant-xxxxx
# 3. 重启Flask服务 (终止 Ctrl+C，重新运行)
# 4. 确保没有多余空格
```

---

### Q3: Web界面无法打开

**症状**: 访问 file://...index.html 是空白

**解决**:
```
1. 确保start.sh还在运行
2. 检查有没有JS错误 (F12打开开发者工具)
3. 尝试 http://localhost:8000 (确保API在运行)
4. 刷新页面 (Cmd+R)
```

---

### Q4: 分析超时（超过2分钟）

**症状**: 论文分析一直在加载

**原因**: 
- 论文太长（> 10000字）
- 网络连接慢
- Claude API繁忙

**解决**:
```bash
# 编辑 backend/config.py
# 改小 CHUNK_SIZE (2000 → 1500)
# 重启服务
```

---

## 🎯 下一步建议

### 完成后做什么？

```
1️⃣ 尝试分析你写的论文
   看看评分和建议

2️⃣ 邀请朋友/同学尝试
   收集反馈

3️⃣ 根据反馈改进
   修改评分标准或提示词

4️⃣ 部署上线
   看DEPLOYMENT_GUIDE.md
   选择发布方案
```

---

## 📞 需要帮助？

| 问题 | 查看文件 |
|------|---------|
| 不知道怎么操作 | `START_HERE.md` |
| 常见问题 | `QUICKSTART.md` |
| 功能文档 | `README.md` |
| 如何发布 | `DEPLOYMENT_GUIDE.md` |
| 系统检查 | 运行 `python test_system.py` |

---

## ✨ VS Code 快捷键速查

| 快捷键 | 功能 |
|-------|------|
| Cmd + O | 打开文件 |
| Cmd + P | 搜索文件 |
| Cmd + ` | 打开/关闭终端 |
| Cmd + S | 保存文件 |
| Cmd + Shift + P | 命令面板 |
| Cmd + / | 注释/取消注释 |
| Cmd + K Cmd + 0 | 关闭所有分组 |

---

**准备好了吗？立即开始！** 👇

```bash
# 在VS Code终端中运行
code /Users/siyuzhang/Desktop/KM/paper-analyzer
```

然后按照上面的5个步骤逐步操作！ 🚀
