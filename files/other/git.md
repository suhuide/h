```c
git config --global alias.diffx 'diff -- ":!.project" ":!.cproject" ":!*.slps" ":!*.pintool" ":!*.html" ":!*.pdm*" ":!*.zap" ":!*.json" ":!*.cmake"'
git config --global alias.diffx 'diff -- ":!.project" ":!.cproject" ":!*.slps" ":!*.pintool" ":!*.html" ":!*.pdm*" ":!*.zap" ":!*.json"'
git config --global alias.diffx 'diff -- ":!.project" ":!.cproject" ":!*.slps" ":!*.pintool" ":!*.html" ":!*.pdm*" ":!*.zap"'
git diff ':!.cproject' ':!*.slps' ':!*.pintool' ':!*.html'
```
```c
git clone --depth 1 https://github.com/openthread/ot-br-posix.git    # Shallow clone (limited history)
git clone --depth 1 --branch "linux-${KERNEL_VERSION}.y" https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git linux    # Clone specific branch with limited history
git clone --recurse-submodules https://github.com/project-chip/connectedhomeip.git    # Clone with submodules

# Git configuration
git config -l                                      # List all git configurations
git config --global user.name "suhuide"           # Set global username
git config --global user.email "suhuide@hoperf.com"    # Set global email
git config --global init.templatedir ~/.git_template    # Set global template directory
git config                                          # Show git configuration

# Log and history
git log                                             # Show commit logs
git log --branches HEAD -p --stat --no-merges --since=2023-12-13 --until=2023-12-22    # Detailed log with date range
git log --branches HEAD --no-merges --since=2025-08-15 --until=2025-09-20    # Log with date range
git rev-parse HEAD                                  # Get current commit hash

# Commit operations
git add .                                           # Add all changes to staging
git commit -m "[TASK_16507][AR01A] xxx"            # Commit with task message

# Push operations
git push                # Push to lens remote

# Pull and fetch
git pull                                            # Pull from remote
git fetch --force origin android11/rk3566           # Force fetch specific branch

# Reset and revert
git reset --hard HEAD^                              # Reset to previous commit (discard last commit)
git reset --hard vendor/etc/firmware/BCM4345C0.hcd  # Reset specific file to HEAD
git rebase FETCH_HEAD                                # Rebase on fetched HEAD
git checkout .                                       # Discard all changes in working directory

# Submodule operations
git submodule update --init                          # Initialize and update submodules
git submodule update --init --recursive              # Initialize and update submodules recursively
git submodule update --init --depth=1 --recursive    # Shallow update of submodules recursively
git submodule update --init --depth=1 --recursive third_party/nlassert/repo third_party/nlio/repo    # Update specific submodules

# Diff operations
git diff                                            # Show changes not staged

# Branch operations
git branch                                          # List local branches
git branch -av                                      # List all branches with last commit

# Status operations
git status                                          # Show working tree status

# Remote add
git remote add origin https://github.com/user/repo.git

# Force checkout remote newest
git checkout <remote-branch-name>          # Switch to remote branch (e.g., git checkout main or git checkout master)
git pull                                    # Pull latest code from remote

git fetch origin                            # Fetch latest code from remote
git reset --hard origin/<remote-branch-name>       # Reset hard to remote branch (e.g., git reset --hard origin/main)
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