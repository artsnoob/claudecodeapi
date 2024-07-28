# Claude Coding Assistant

Claude Coding Assistant is a Python-based command-line interface (CLI) application that allows users to interact with Claude, an AI language model developed by Anthropic. This tool is particularly useful for developers and coding enthusiasts who want to leverage Claude's capabilities for coding assistance, problem-solving, and general AI interactions.

## Features

- Interactive chat interface with Claude
- Support for multiline input, ideal for pasting code snippets
- Preserved formatting for code blocks in Claude's responses
- Color-coded output for enhanced readability
- Conversation management (clear chat history, exit chat)
- Error handling for API calls

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An Anthropic API key (sign up at [Anthropic's website](https://www.anthropic.com) if you don't have one)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/claude-coding-assistant.git
   cd claude-coding-assistant
   ```

2. Install the required Python packages:
   ```
   pip install anthropic colorama
   ```

3. Set up your Anthropic API key as an environment variable:
   - On Unix-like systems:
     ```
     export ANTHROPIC_API_KEY='your-api-key-here'
     ```
   - On Windows:
     ```
     set ANTHROPIC_API_KEY=your-api-key-here
     ```

## Usage

To start the Claude Coding Assistant, run:

```
python claude_assistant.py
```

Once the application starts, you'll see a welcome message and instructions. Here are the key commands:

- Type your message or code, then enter `###` on a new line to send it to Claude.
- Use triple backticks (```) to denote code blocks for proper formatting.
- Type `/clear` to start a new conversation.
- Type `exit` or `quit` to end the chat session.

## Example Interaction

```
Welcome to the Claude Coding Assistant!
• Type 'exit' or 'quit' to end the chat.
• Use triple backticks (```) to denote code blocks.
• Type '/clear' to start a new conversation.
• Type '###' on a new line to end your input and send it to Claude.

Your message (type '###' on a new line to end input):
> Can you show me a Python function to calculate the factorial of a number?
> ###

Claude's Response:
Certainly! Here's a Python function to calculate the factorial of a number:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
```

This function uses recursion to calculate the factorial. Here's how it works:

1. If the input `n` is 0 or 1, the function returns 1 (as 0! and 1! are both defined as 1).
2. For any other positive integer, it recursively calls itself with `n-1` and multiplies the result by `n`.

You can use this function by calling `factorial(n)` with any non-negative integer `n`. The example usage shows how to calculate the factorial of 5.

Your message (type '###' on a new line to end input):
> exit

Goodbye!
```
