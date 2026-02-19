# Day 27 – GitHub Profile Makeover: Build Your Developer Identity

## Objective

Today I worked on improving my GitHub profile so it clearly represents my DevOps learning journey, projects, and technical growth.

The goal was to make my GitHub profile look more professional and useful for recruiters, hiring managers, and other developers who visit my profile.

---

## Task 1: GitHub Profile Audit

### Current Profile Review

I reviewed my GitHub profile as if I were a recruiter or another developer visiting it for the first time.

### Audit Questions

| Check                            | Status                    | Notes                                                                           |
| -------------------------------- | ------------------------- | ------------------------------------------------------------------------------- |
| Profile picture is professional  | To be updated / Completed | I checked whether my profile photo looks clear and professional.                |
| Bio is filled in                 | To be updated / Completed | I reviewed whether my bio clearly explains that I am learning DevOps and Cloud. |
| Pinned repositories are relevant | To be updated / Completed | I checked if the pinned repos represent my best DevOps work.                    |
| Repositories have descriptions   | To be updated / Completed | I checked whether important repos have clear one-line descriptions.             |
| Repositories have README files   | To be updated / Completed | I verified that key repos explain what they contain.                            |
| Recruiter can understand my work | To be updated / Completed | I checked whether my GitHub profile shows my current learning path clearly.     |

### First Impression Before Changes

Before the makeover, my GitHub profile needed better organization. Some repositories needed clearer descriptions, better README files, and more professional presentation.

---

## Task 2: Profile README

### Special Profile Repository

I created or updated a special GitHub repository with the same name as my GitHub username.

Example format:

```text
https://github.com/<github-username>/<github-username>
```

This repository contains a `README.md` file that appears directly on my GitHub profile page.

### Profile README Content Added

The profile README includes:

- Short introduction about who I am
- Current learning focus
- 90 Days of DevOps journey
- Skills and tools I am learning
- Important repository links
- Contact links

### Sample Profile README

```markdown
# Hi, I'm Preetham

I'm learning DevOps and Cloud with a strong focus on hands-on practice, automation, and real-world engineering workflows.

## Currently Working On

- 90 Days of DevOps challenge
- Linux, Git, GitHub, Shell Scripting, Python, Docker, Kubernetes, CI/CD, AWS, and Monitoring
- Building practical DevOps projects and documenting my progress daily

## Skills I'm Learning

- Linux fundamentals
- Git and GitHub workflows
- Shell scripting
- Python for DevOps automation
- Docker and containers
- Kubernetes basics
- CI/CD pipelines
- AWS Cloud fundamentals
- Monitoring and logging

## Featured Repositories

- [90-days-of-devops](https://github.com/<github-username>/90-days-of-devops)
- [shell-scripts](https://github.com/<github-username>/shell-scripts)
- [python-scripts](https://github.com/<github-username>/python-scripts)
- [devops-notes](https://github.com/<github-username>/devops-notes)

## Connect With Me

- GitHub: https://github.com/<github-username>
- LinkedIn: https://linkedin.com/in/<linkedin-username>
- Email: your-email@example.com
```

---

## Task 3: Repository Organization

I reviewed and organized my repositories to make them easier to understand.

### Repository Naming Standard

I used clear repository names with hyphens instead of spaces.

Examples:

```text
90-days-of-devops
shell-scripts
python-scripts
devops-notes
```

---

### Repository 1: 90 Days of DevOps

**Repository name:** `90-days-of-devops`

**Purpose:** Main repository for my 90 Days of DevOps learning journey.

**Improvements made:**

- Added or improved the main README
- Organized daily work by day
- Added clear explanations for daily tasks
- Ensured project structure is easy to follow

**Suggested description:**

```text
My hands-on 90 Days of DevOps journey with daily tasks, notes, scripts, and projects.
```

---

### Repository 2: Shell Scripts

**Repository name:** `shell-scripts`

**Purpose:** Dedicated repository for Bash and shell scripting practice.

**Content included:**

- Day 16 shell scripting basics
- Day 17 loops, arguments, and error handling
- Day 18 functions and intermediate scripting
- Day 19 log rotation, backup, and crontab
- Day 20 log analyzer project
- Day 21 shell scripting cheat sheet

**Suggested description:**

```text
Practical shell scripts for Linux automation, log analysis, backups, and DevOps tasks.
```

---

### Repository 3: Python Scripts

**Repository name:** `python-scripts`

**Purpose:** Dedicated repository for Python automation projects.

**Content included:**

- Python basics for DevOps
- API automation scripts
- File handling and log analysis
- OOP-based log analyzer
- CLI tools using argparse
- AWS automation with Boto3
- FastAPI DevOps automation project

**Suggested description:**

```text
Python automation scripts and mini-projects for DevOps, APIs, logs, and cloud workflows.
```

---

### Repository 4: DevOps Notes

**Repository name:** `devops-notes`

**Purpose:** Central place for my learning notes, references, and cheat sheets.

**Content included:**

- Git commands
- Shell scripting cheat sheet
- Linux notes
- Python notes
- DevOps concepts

**Suggested description:**

```text
Personal DevOps notes, cheat sheets, commands, and learning references.
```

---

## Task 4: Pinned Repositories

I selected 6 repositories that best represent my learning and hands-on work.

### Selected Pinned Repositories

| Repository                  | Why I pinned it                                     |
| --------------------------- | --------------------------------------------------- |
| `90-days-of-devops`         | Shows my complete DevOps learning journey.          |
| `shell-scripts`             | Shows Linux automation and Bash scripting practice. |
| `python-scripts`            | Shows Python automation for DevOps tasks.           |
| `devops-notes`              | Shows my documentation and learning consistency.    |
| `devops-git-practice`       | Shows hands-on Git and GitHub workflow practice.    |
| `fastapi-devops-automation` | Shows API-based DevOps automation work.             |

---

## Task 5: Cleanup

### Cleanup Actions

I reviewed my repositories and checked for:

- Empty repositories
- Abandoned repositories
- Random forks
- Repositories without README files
- Repositories without descriptions
- Unclear repository names
- Exposed secrets such as `.env`, API keys, passwords, or tokens

### Secret Safety Checklist

| Check                                     | Status         |
| ----------------------------------------- | -------------- |
| `.env` files are not committed            | To be verified |
| API keys are not exposed                  | To be verified |
| Passwords are not exposed                 | To be verified |
| `.gitignore` exists where needed          | To be verified |
| Commit history checked for sensitive data | To be verified |

### Useful Commands Used

```bash
# Check tracked files
 git ls-files

# Search for possible secrets
 grep -R "password\|secret\|token\|api_key\|API_KEY" .

# Check Git history quickly
 git log --oneline

# Check repository status
 git status
```

---

## Task 6: Before and After

### Before Screenshot

Add the screenshot of the GitHub profile before making changes.

```markdown
![GitHub Profile Before](./screenshots/github-profile-before.png)
```

### After Screenshot

Add the screenshot of the GitHub profile after making changes.

```markdown
![GitHub Profile After](./screenshots/github-profile-after.png)
```

---

## Three Improvements I Made

### 1. Improved Profile README

I added a clean GitHub profile README that explains who I am, what I am learning, and what projects I am working on.

**Why:** This helps visitors quickly understand my DevOps learning journey.

---

### 2. Organized Important Repositories

I reviewed my repositories and focused on clear names, descriptions, README files, and proper structure.

**Why:** Organized repositories make my work easier to understand and look more professional.

---

### 3. Selected Better Pinned Repositories

I pinned repositories that show practical DevOps skills such as Git, Shell scripting, Python automation, and documentation.

**Why:** Pinned repositories are the first projects people notice on my profile, so they should represent my best work.

---

## Final GitHub Profile Link

```text
https://github.com/<github-username>
```

---

## LinkedIn Learn in Public Post Draft

```text
Day 27 of my 90 Days of DevOps journey

Today was a GitHub Profile Makeover day.

I improved my GitHub profile README, cleaned up repositories, added better repo descriptions, reviewed pinned repositories, and made my profile easier to understand for recruiters and other developers.

Key improvements:
- Added a clean profile README
- Organized DevOps learning repositories
- Improved repo descriptions and documentation
- Checked for secrets and unnecessary files

This helped me understand that GitHub is not just a code hosting platform. It is also a developer portfolio.

#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham #GitHub #DevOps
```

---

## Final Notes

Today helped me understand that a professional GitHub profile is important for building a developer identity. Clean repositories, proper README files, and consistent documentation make my work more visible and easier to evaluate.
