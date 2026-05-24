# Contributing to Paper Analyzer

Thank you for your interest in contributing to Paper Analyzer! This document provides guidelines and instructions for contributing to the project.

## 🤝 Code of Conduct

Please be respectful and constructive in all interactions. We aim to maintain an inclusive and welcoming environment for all contributors.

## 📝 How to Report Issues

### Before Reporting
- Check existing issues to avoid duplicates
- Read the documentation and FAQ
- Test with the latest version
- Gather relevant information (error messages, OS, Python version, etc.)

### Issue Report Template
```
**Title:** Clear, descriptive title

**Environment:**
- OS: [macOS/Linux/Windows]
- Python: [version]
- Paper Analyzer: [version]

**Description:**
Describe the issue clearly and concisely.

**Steps to Reproduce:**
1. First step
2. Second step
3. ...

**Expected Behavior:**
What should happen?

**Actual Behavior:**
What actually happens?

**Error Messages:**
[Include full error traceback]

**Screenshots:**
[If applicable]
```

## 🚀 Contributing Code

### Getting Started
1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature
4. Make your changes
5. Submit a pull request

### Branch Naming Convention
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### Code Style Guidelines

**Python Code**
- Follow PEP 8 conventions
- Use type hints where appropriate
- Include docstrings for functions and classes
- Maximum line length: 88 characters (Black formatter compatible)
- Use meaningful variable names

**Example:**
```python
async def analyze_thesis(file_path: str) -> dict[str, any]:
    """
    Analyze a thesis PDF and return evaluation scores.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        Dictionary containing analysis results
        
    Raises:
        FileNotFoundError: If PDF file doesn't exist
        ValueError: If PDF is corrupted
    """
    pass
```

**JavaScript/HTML**
- Use 2-space indentation
- Use descriptive class and ID names
- Comment complex logic
- Keep functions small and focused

### Commit Message Standards

Write clear, descriptive commit messages:

```
[Type] Short description (50 chars max)

Longer explanation of the changes made, why they were
necessary, and any relevant context. Wrap at 72 characters.

Fixes #123
Relates to #456
```

**Commit Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Code style (no functional changes)
- `refactor:` Code refactoring
- `perf:` Performance improvements
- `test:` Adding or updating tests
- `chore:` Build, dependency updates

### Before Submitting a Pull Request

- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated if needed
- [ ] No debug code or print statements
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

## 🧪 Testing

### Run Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run all tests
pytest

# Run with coverage
pytest --cov=backend
```

### Testing Guidelines
- Write tests for new features
- Maintain >80% code coverage
- Test edge cases and error conditions
- Use descriptive test names

## 📚 Documentation

### Updating Documentation
- Keep README.md in sync with code changes
- Update docstrings when modifying functions
- Add examples for new features
- Document breaking changes clearly

### Documentation Style
- Use clear, concise language
- Include code examples
- Add diagrams where helpful
- Link to related documentation

## 🔍 Review Process

### What Happens Next
1. A maintainer reviews your PR
2. Feedback is provided if changes are needed
3. You make requested changes
4. Once approved, PR is merged

### Review Criteria
- Code quality and style compliance
- Test coverage
- Documentation completeness
- Performance impact
- Security considerations

## 🎯 Priority Areas for Contribution

### High Priority
- Bug fixes for reported issues
- Performance improvements
- Security enhancements
- Documentation improvements

### Medium Priority
- New features with clear specifications
- Code refactoring
- Test coverage expansion

### Great for First-Time Contributors
- Documentation improvements
- Adding examples
- Writing tests
- Bug fixes marked as "good first issue"

## 📋 Development Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/paper-analyzer.git
cd paper-analyzer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt
pip install -e ".[dev]"

# Set up pre-commit hooks (optional but recommended)
pre-commit install

# Start developing
git checkout -b feature/your-feature
```

## 🚀 Deployment

Changes to `main` branch are automatically deployed. Ensure:
- All tests pass
- Documentation is updated
- No breaking changes without notice

## 📞 Questions?

- Check the [documentation](./README.md)
- Review existing issues and discussions
- Ask in a new issue with `[Question]` prefix

## 🙏 Thank You!

Your contributions make this project better. We appreciate your time and effort!

---

**Happy Contributing!** 🎉
