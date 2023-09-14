# <span style="color:#FF5733;">🚀 Git Repository Guidelines</span>

Welcome to our Git repository! This document outlines the best practices for contributing to this project. Please follow these guidelines to maintain a clean and organized repository.

## <span style="color:#008000;">🌟 Do's</span>

### 1. <span style="color:#008000;">Create an Issue First</span>

Before making any code changes, create a GitHub issue to discuss the problem or feature you plan to address. This ensures clear communication and helps in tracking progress.

### 2. <span style="color:#008000;">Create Feature or Bugfix Branches</span>

For each issue or task, create a dedicated branch from the `main` branch. Use descriptive branch names like `feature/new-feature` or `bugfix/issue-description`.

```bash
git checkout -b feature/new-feature
```

### 3. <span style="color:#008000;">Keep Commits Atomic</span>

Make commits small and focused on a single task. Each commit should address one issue or feature. Use descriptive commit messages that start with a verb.

```bash
git commit -m "✨ Add user registration functionality"
```

### 4. <span style="color:#008000;">Pull from `main` Frequently</span>

Regularly pull the latest changes from the `main` branch into your feature branch to avoid conflicts and stay up-to-date with the project's progress.

```bash
git pull origin main
```

### 5. <span style="color:#008000;">Use Feature Branches for Pull Requests</span>

Submit pull requests (PRs) from your feature branches to the `main` branch. PRs undergo code reviews before merging.

### 6. <span style="color:#008000;">Write Tests</span>

For new features and bug fixes, write unit tests whenever applicable. Ensure that existing tests pass before committing.

### 7. <span style="color:#008000;">Document Code Changes</span>

Update code comments and documentation to reflect changes. This helps maintain code readability and makes it easier for others to understand your code.

## <span style="color:#FF5733;">🚫 Don'ts</span>

### 1. <span style="color:#FF0000;">Don't Commit Directly to `main`</span>

Avoid committing directly to the `main` branch. Use feature branches and submit PRs for code review.

### 2. <span style="color:#FF0000;">Don't Push Sensitive Information</span>

Never push sensitive information like API keys, passwords, or secrets to the repository. Use environment variables or configuration files for such information.

### 3. <span style="color:#FF0000;">Don't Skip Code Reviews</span>

Always seek code reviews from team members before merging a PR. This ensures code quality and consistency.

### 4. <span style="color:#FF0000;">Don't Merge Your Own PRs</span>

To maintain code quality and transparency, don't merge your own PRs. Another team member should review and merge them.

### 5. <span style="color:#FF0000;">Don't Forget to Pull Before Pushing</span>

Before pushing your changes, always pull the latest changes from the `main` branch to avoid conflicts.

## <span style="color:#FF5733;">💬 Questions and Feedback</span>

If you have questions or suggestions regarding our Git practices, please reach out to the team on our WhatsApp group. Happy coding!