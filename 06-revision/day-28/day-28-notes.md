# Day 28 – Revision Day: Everything from Day 1 to Day 27

## Overview

Day 28 is a revision day for everything learned from Day 1 to Day 27 of the 90DaysOfDevOps journey.

The goal of this day is to pause, review previous topics, identify weak areas, and make sure I can explain and use the concepts confidently in real-world DevOps scenarios.

---

## Topics Covered So Far

| Days       | Topic                          | Key Concepts                                                            |
| ---------- | ------------------------------ | ----------------------------------------------------------------------- |
| Day 1      | DevOps & Cloud Introduction    | DevOps basics, SDLC, cloud computing                                    |
| Days 2–7   | Linux Fundamentals             | Linux commands, processes, systemd, file system, troubleshooting        |
| Day 8      | Cloud Server Setup             | Docker, Nginx, basic web deployment                                     |
| Days 9–11  | Users, Permissions & Ownership | Users, groups, chmod, chown, chgrp                                      |
| Day 12     | Revision Day 1                 | Recap of Days 1–11                                                      |
| Day 13     | Volume Management              | LVM, physical volumes, volume groups, logical volumes                   |
| Days 14–15 | Networking                     | DNS, IP, subnets, ports, connectivity checks                            |
| Days 16–18 | Shell Scripting                | Variables, conditions, loops, arguments, functions, error handling      |
| Days 19–20 | Shell Scripting Projects       | Log rotation, backup, crontab, log analyzer                             |
| Day 21     | Shell Scripting Cheat Sheet    | Personal shell scripting reference                                      |
| Days 22–25 | Git & GitHub                   | Git basics, branching, merge, rebase, stash, cherry-pick, reset, revert |
| Day 26     | GitHub CLI                     | Managing GitHub using terminal commands                                 |
| Day 27     | GitHub Profile                 | Developer branding, profile README, repo cleanup                        |

---

## Task 1: Self-Assessment Checklist

### Linux

| Skill                                                                   | Status             |
| ----------------------------------------------------------------------- | ------------------ |
| Navigate the file system, create/move/delete files and directories      | Can do confidently |
| Manage processes — list, kill, background/foreground                    | Can do confidently |
| Work with systemd — start, stop, enable, check status of services       | Can do confidently |
| Read and edit text files using vi/vim or nano                           | Can do confidently |
| Troubleshoot CPU, memory, and disk issues using top, free, df, du       | Can do confidently |
| Explain the Linux file system hierarchy                                 | Need to revisit    |
| Create users and groups, manage passwords                               | Can do confidently |
| Set file permissions using chmod                                        | Can do confidently |
| Change file ownership with chown and chgrp                              | Can do confidently |
| Create and manage LVM volumes                                           | Need to revisit    |
| Check network connectivity using ping, curl, netstat, ss, dig, nslookup | Can do confidently |
| Explain DNS resolution, IP addressing, subnets, and common ports        | Need to revisit    |

### Shell Scripting

| Skill                                                      | Status             |
| ---------------------------------------------------------- | ------------------ |
| Write a script with variables, arguments, and user input   | Can do confidently |
| Use if/elif/else and case statements                       | Can do confidently |
| Write for, while, and until loops                          | Can do confidently |
| Define and call functions with arguments and return values | Can do confidently |
| Use grep, awk, sed, sort, uniq for text processing         | Need to revisit    |
| Handle errors with set -e, set -u, set -o pipefail, trap   | Need to revisit    |
| Schedule scripts with crontab                              | Can do confidently |

### Git & GitHub

| Skill                                                      | Status             |
| ---------------------------------------------------------- | ------------------ |
| Initialize a repo, stage, commit, and view history         | Can do confidently |
| Create and switch branches                                 | Can do confidently |
| Push to and pull from GitHub                               | Can do confidently |
| Explain clone vs fork                                      | Can do confidently |
| Merge branches and understand fast-forward vs merge commit | Can do confidently |
| Rebase a branch and explain when to use it vs merge        | Need to revisit    |
| Use git stash and git stash pop                            | Can do confidently |
| Cherry-pick a commit from another branch                   | Can do confidently |
| Explain squash merge vs regular merge                      | Need to revisit    |
| Use git reset and git revert                               | Can do confidently |
| Explain GitFlow, GitHub Flow, and Trunk-Based Development  | Need to revisit    |
| Use GitHub CLI to create repos, PRs, and issues            | Can do confidently |

---

## Task 2: Weak Spots to Revisit

I selected the following three topics to revise again:

### 1. LVM Volume Management

#### Why I need to revisit it

LVM is powerful but has multiple layers: physical volumes, volume groups, and logical volumes. I need more hands-on practice to become fully confident.

#### What I re-learned

- A physical volume is the actual disk or partition used by LVM.
- A volume group combines one or more physical volumes.
- A logical volume is created from the volume group and used like a normal partition.
- LVM is useful because it allows easier resizing and flexible storage management.

#### Commands revised

```bash
sudo pvcreate /dev/sdb
sudo vgcreate devops-vg /dev/sdb
sudo lvcreate -L 5G -n devops-lv devops-vg
sudo mkfs.ext4 /dev/devops-vg/devops-lv
sudo mount /dev/devops-vg/devops-lv /mnt/devops
```

---

### 2. DNS, IP Addressing, Subnets, and Ports

#### Why I need to revisit it

Networking is important for troubleshooting servers, applications, cloud deployments, and Kubernetes services.

#### What I re-learned

- DNS converts domain names into IP addresses.
- IP addresses identify devices on a network.
- Subnets divide a network into smaller network ranges.
- Ports help applications communicate on the same machine.
- Common ports include 22 for SSH, 80 for HTTP, 443 for HTTPS, and 53 for DNS.

#### Commands revised

```bash
ping google.com
curl -I https://google.com
nslookup google.com
dig google.com
ss -tulnp
netstat -tulnp
```

---

### 3. Git Rebase vs Merge

#### Why I need to revisit it

Both merge and rebase are used to integrate branch changes, but they affect Git history differently.

#### What I re-learned

- `git merge` keeps branch history and creates a merge commit when needed.
- `git rebase` rewrites commit history by placing commits on top of another branch.
- Merge is safer for shared branches.
- Rebase is useful for keeping a clean linear history before opening a pull request.

#### Commands revised

```bash
git checkout feature-branch
git merge main

git checkout feature-branch
git rebase main
```

---

## Task 3: Quick-Fire Questions

### 1. What does `chmod 755 script.sh` do?

`chmod 755 script.sh` gives:

- Owner: read, write, execute
- Group: read and execute
- Others: read and execute

This is commonly used for scripts that should be executable by everyone but only editable by the owner.

```bash
chmod 755 script.sh
```

---

### 2. What is the difference between a process and a service?

A process is any running program on a system.

A service is usually a background process managed by the system, often through `systemd`. Services are commonly used for long-running applications like Nginx, Docker, SSH, and databases.

Example:

```bash
ps aux
systemctl status nginx
```

---

### 3. How do you find which process is using port 8080?

```bash
sudo lsof -i :8080
```

Alternative commands:

```bash
sudo ss -tulnp | grep 8080
sudo netstat -tulnp | grep 8080
```

---

### 4. What does `set -euo pipefail` do in a shell script?

`set -euo pipefail` makes shell scripts safer.

- `set -e`: exits the script if a command fails
- `set -u`: exits if an undefined variable is used
- `set -o pipefail`: makes a pipeline fail if any command in the pipeline fails

Example:

```bash
#!/bin/bash
set -euo pipefail
```

---

### 5. What is the difference between `git reset --hard` and `git revert`?

`git reset --hard` moves the branch pointer and removes changes from the working directory. It rewrites history and can be dangerous on shared branches.

`git revert` creates a new commit that undoes a previous commit. It is safer for shared branches because it does not rewrite history.

```bash
git reset --hard HEAD~1
git revert <commit-hash>
```

---

### 6. What branching strategy would you recommend for a team of 5 developers shipping weekly?

For a small team shipping weekly, I would recommend GitHub Flow.

Reason:

- It is simple and easy to follow.
- Developers create short-lived feature branches.
- Changes are reviewed through pull requests.
- The `main` branch stays production-ready.
- It works well for frequent releases.

---

### 7. What does `git stash` do and when would you use it?

`git stash` temporarily saves uncommitted changes so I can switch branches or pull updates without committing unfinished work.

Example:

```bash
git stash
git checkout main
git pull
git checkout feature-branch
git stash pop
```

---

### 8. How do you schedule a script to run every day at 3 AM?

Open crontab:

```bash
crontab -e
```

Add this line:

```bash
0 3 * * * /path/to/script.sh
```

This runs the script every day at 3:00 AM.

---

### 9. What is the difference between `git fetch` and `git pull`?

`git fetch` downloads changes from the remote repository but does not merge them into the current branch.

`git pull` downloads changes and automatically merges or rebases them into the current branch.

```bash
git fetch origin
git pull origin main
```

---

### 10. What is LVM and why would you use it instead of regular partitions?

LVM stands for Logical Volume Manager.

It is used to manage disk storage more flexibly than regular partitions. With LVM, we can resize volumes, combine disks, and manage storage more easily without depending only on fixed partitions.

---

## Task 4: Organize Your Work

### Repository Cleanup Checklist

| Task                                         | Status    |
| -------------------------------------------- | --------- |
| Day 1 to Day 27 submissions committed        | Completed |
| Day 1 to Day 27 submissions pushed to GitHub | Completed |
| `git-commands.md` updated                    | Completed |
| Shell scripting cheat sheet completed        | Completed |
| GitHub profile README updated                | Completed |
| Repositories renamed and organized properly  | Completed |
| Important repositories pinned                | Completed |
| Repository descriptions added                | Completed |

---

## Task 5: Teach It Back

### Topic: Git Branching Explained Simply

Git branching allows developers to work on new features or fixes without directly changing the main project.

Think of the `main` branch as the stable version of the project. When a developer wants to add a new feature, they create a separate branch. They can safely make changes there without breaking the main code.

After the work is completed and tested, the branch can be merged back into `main`. This keeps the project organized and allows teams to work on multiple tasks at the same time.

In real DevOps teams, branches are commonly used for features, bug fixes, hotfixes, and experiments.

Example:

```bash
git checkout -b feature-login
# make changes
git add .
git commit -m "feat: add login feature"
git checkout main
git merge feature-login
```

---

## Key Takeaways

- Revision is important before moving to advanced DevOps topics.
- Linux, scripting, networking, and Git are core DevOps foundations.
- Weak areas should be practiced again with hands-on tasks.
- Git history management is important for real team collaboration.
- Shell scripting becomes more powerful when combined with cron and Linux commands.
- Teaching a concept back is a good way to test real understanding.

---

## Final Reflection

Day 28 helped me understand how much I have learned in the first 27 days of this DevOps journey.

I now feel more confident with Linux commands, Git workflows, shell scripting, GitHub, and basic networking. I also identified important areas like LVM, networking, and Git rebase that need more hands-on practice.

Going forward, I will continue revising weak areas while building more real-world DevOps projects.
