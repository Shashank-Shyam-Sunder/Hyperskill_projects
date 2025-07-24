# Regular Expressions in Python

## Overview
This project is a comprehensive collection of examples and exercises demonstrating the use of regular expressions (regex) in Python. It covers various regex functions, patterns, and techniques for text matching, searching, and manipulation.

## Features
- Pattern matching with `re.match()` for matching at the beginning of strings
- Searching with `re.search()` for finding patterns anywhere in strings
- Finding all occurrences with `re.findall()`
- Text substitution with `re.sub()`
- String splitting with `re.split()`
- Various regex patterns and concepts:
  - Basic character matching
  - Character classes with `[]`
  - Escaping special characters with `\`
  - Quantifiers like `?`, `+`, `{1,2}`
  - Anchors like `$` for end of string
  - Shorthand character classes like `\w`
  - Alternation with `|`
  - Capturing groups with `()`
- Regex flags:
  - `re.IGNORECASE` for case-insensitive matching
  - `re.DOTALL` to make `.` match newlines

## How It Works
The project consists of numerous examples that demonstrate different aspects of regular expressions:

1. Basic pattern matching with `re.match()` to check if a string starts with a pattern
2. Using character classes to match specific sets of characters
3. Escaping special characters in regex patterns
4. Using quantifiers to specify how many times a pattern should match
5. Working with anchors to match positions in strings
6. Using shorthand character classes for common patterns
7. Applying regex flags to modify matching behavior
8. Capturing and extracting parts of matched text with groups
9. Substituting text based on patterns
10. Splitting strings using regex patterns

## Usage Examples

### Basic Matching
```python
import re

# Check if a string starts with a pattern
result = re.match('hedge', 'hedgehog')
print(result is None)  # False - 'hedge' is at the beginning of 'hedgehog'

result = re.match('hog', 'hedgehog')
print(result is None)  # True - 'hog' is not at the beginning of 'hedgehog'
```

### Character Classes
```python
import re
template = r"[1-9a-fA-F]{1,2}$"

# Match hexadecimal values
print(re.match(template, "A1"))  # Match
print(re.match(template, "G1"))  # No match - 'G' is not a hex digit
```

### Substitution
```python
import re
string = "@some_twitter_user I love dogs, @another_twitter_user!"
pattern = r'@\w+'
replaced_string = re.sub(pattern, "<AUTHOR>", string, count=1)
final_string = re.sub(pattern, "<HANDLE>", replaced_string)

print(final_string)  # "<AUTHOR> I love dogs, <HANDLE>!"
```

### Group Capturing
```python
import re
string = "Something\n<START>\nsomething\n<END>\nsomething"
pattern = r"<START>(.+)<END>"

match = re.search(pattern, string, flags=re.DOTALL)
if match:
    print(match.group(1))  # "\nsomething\n"
```

## Skills Demonstrated
- Regular expression pattern creation and usage
- Text pattern matching and extraction
- String manipulation with regex
- Using regex flags to modify matching behavior
- Error handling in pattern matching
- Working with capturing groups
- Substituting text based on patterns
- Splitting strings using regex

## Requirements
- Python 3.6 or higher
- `re` module (included in Python standard library)

You can install the required dependencies using:
```bash
pip install -r requirements_regexps_python.txt
```

## Learning Resources
- [Python re Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)