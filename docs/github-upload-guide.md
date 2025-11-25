# 将本项目上传到 GitHub 的步骤

以下步骤假设你已经在本地完成了开发，并希望把当前仓库推送到 GitHub。若尚未登录 GitHub 或没有仓库，请先完成账号准备。

## 1. 创建远程仓库
1. 登录 GitHub，点击右上角 **New repository**。
2. 填写仓库名称（如 `awesome-cloudflare`），保持 **Public/Private** 按需选择。
3. 创建完成后，复制仓库的 HTTPS 或 SSH 地址。

## 2. 设置远程地址
在项目根目录执行：
```bash
git remote add origin <你的仓库地址>
```
如果之前已设置过 `origin`，可先移除或修改：
```bash
git remote remove origin
# 或
# git remote set-url origin <你的仓库地址>
```

## 3. 推送当前分支
确保工作区已提交（`git status` 无待提交文件）后执行：
```bash
git push -u origin $(git branch --show-current)
```
若提示需要登录，可按提示使用 PAT（Personal Access Token）或 SSH key。

## 4. 推送后续更新
以后每次提交后直接推送：
```bash
git push
```

## 5. 常见问题
- **权限不足/认证失败**：检查是否使用了有效的 PAT 或配置了 SSH key。
- **被拒绝推送（non-fast-forward）**：先 `git pull --rebase origin <branch>` 同步，再推送。
- **大文件限制**：尽量避免提交超过 GitHub 限制的二进制模型文件，可使用 Git LFS。

完成以上步骤后，GitHub 仓库即可同步当前代码，并可继续创建 PR、添加协作者或配置 CI/CD。
