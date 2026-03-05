```c
$ git config --global user.name "suhuide"
$ git config --global user.email suhuide@hoperf.com
```
```c
git config --global alias.diffx 'diff -- ":!.project" ":!.cproject" ":!*.slps" ":!*.pintool" ":!*.html" ":!*.pdm*" ":!*.zap"'
git diff ':!.cproject' ':!*.slps' ':!*.pintool' ':!*.html'
```
```c
git tag
git fetch --tags
git checkout tags/v2.8.0 -f
```
```c
git reset --hard HEAD   # Remove all uncommitted changes
git switch -            # Return to the previous branch
git checkout -          # Return to the previous branch
git branch -r           # Check remote branches
git branch -a           # Check all branches (local + remote)
git remote -v           # Show all remote repositories' names and URLs
```
```c
git remote add origin https://github.com/user/repo.git
```

```c
1. 删除当前的 submodule
bash
# 1. 从 git 中移除 submodule
git rm --cached aok02_common

# 2. 删除 .gitmodules 中的相关配置
git config -f .gitmodules --remove-section submodule.aok02_common

# 3. 从 .git/config 中移除 submodule 配置
git config --remove-section submodule.aok02_common

# 4. 删除实际目录（如果存在）
rm -rf aok02_common

# 5. 删除 git 的 submodule 目录
rm -rf .git/modules/aok02_common
2. 重新添加为 common/
bash
# 重新添加 submodule，指定目录名为 common/
git submodule add git@hoperf-matter:matter/customerproject/aok02_common.git common
3. 提交更改
bash
# 查看状态确认
git status

# 提交更改
git add .gitmodules common
git commit -m "fix: rename submodule from aok02_common to common"
```
## git account
```c
suhuide@hoperf.com
Shd**475967
```