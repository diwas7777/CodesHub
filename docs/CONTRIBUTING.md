# Contributing Guidelines

## Overview
We welcome contributions that improve code organization, add meaningful examples, or enhance documentation.

## File Organization Standards

### Directory Structure
- Place files in appropriate category directories
- Create new categories when needed
- Maintain consistent structure across languages

### Naming Conventions
- **Python**: `snake_case.py`
- **JavaScript**: `camelCase.js`
- **Java**: `PascalCase.java`
- **C/C++**: `snake_case.c/.cpp`

### File Requirements
1. **Header Comment**: Include purpose, author, complexity
2. **Documentation**: Clear function/class documentation
3. **Examples**: Include usage examples
4. **Error Handling**: Proper exception handling
5. **Testing**: Include test cases or example runs

## Code Quality Standards

### Python Specific
```python
"""
Module: algorithm_name.py
Description: Brief description of the algorithm/utility
Author: Your Name
Date: YYYY-MM-DD
Complexity: Time O(n), Space O(1)

Example:
    >>> from algorithm_name import function_name
    >>> result = function_name([1, 2, 3, 4, 5])
    >>> print(result)
    Expected Output
"""

def function_name(parameter):
    """
    Brief function description.
    
    Args:
        parameter (type): Description of parameter
        
    Returns:
        type: Description of return value
        
    Raises:
        ValueError: When parameter is invalid
    """
    # Implementation here
    pass

# Example usage
if __name__ == "__main__":
    # Test cases and examples
    pass
```

## Pull Request Process

1. **Fork** the repository
2. **Create feature branch**: `git checkout -b feature/category-name`
3. **Make changes** following guidelines
4. **Test thoroughly**
5. **Update documentation**
6. **Submit pull request**

### PR Requirements
- [ ] Code follows naming conventions
- [ ] Proper directory placement
- [ ] Documentation included
- [ ] Examples provided
- [ ] README updated if necessary
- [ ] No duplicate functionality

## Directory Creation Guidelines

When creating new directories:
1. Use descriptive, lowercase names with hyphens
2. Include comprehensive README.md
3. Organize by functionality, not complexity
4. Maintain parallel structure across languages

## Review Process

All contributions will be reviewed for:
- Code quality and style
- Proper organization
- Documentation completeness
- Educational value
- No security vulnerabilities
