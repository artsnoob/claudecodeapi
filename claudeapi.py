import textwrap
import anthropic
import os
import shutil
from typing import List, Dict
from colorama import init, Fore, Back, Style

init(autoreset=True)

class ClaudeCodingAssistant:
    MODEL = "claude-3-5-sonnet-20240620"
    MAX_TOKENS = 4096
    
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.messages: List[Dict[str, str]] = []
        self.terminal_width = shutil.get_terminal_size().columns

    def get_multiline_input(self) -> str:
        print(f"\n{Fore.YELLOW}Your message (type '###' on a new line to end input):")
        lines = []
        while True:
            try:
                line = input(f"{Fore.YELLOW}> {Fore.RESET}")
                if line.strip() == '###':
                    break
                lines.append(line)
            except EOFError:
                break
        return "\n".join(lines)

    def print_response(self, message: str):
        print(f"\n{Fore.GREEN}Claude's Response:")
        in_code_block = False
        code_block_lines = []
        
        for line in message.split("\n"):
            if line.strip().startswith("```"):
                if in_code_block:
                    # End of code block, print it with full-width white background
                    print(f"{Fore.BLACK}{Back.WHITE}{' ' * self.terminal_width}")
                    for code_line in code_block_lines:
                        padded_line = code_line.ljust(self.terminal_width)
                        print(f"{Fore.BLACK}{Back.WHITE}{padded_line}{Style.RESET_ALL}")
                    print(f"{Fore.BLACK}{Back.WHITE}{' ' * self.terminal_width}{Style.RESET_ALL}")
                    code_block_lines = []
                else:
                    # Start of code block
                    print(f"{Fore.BLACK}{Back.WHITE}{' ' * self.terminal_width}")
                    print(f"{Fore.BLACK}{Back.WHITE}{line.ljust(self.terminal_width)}{Style.RESET_ALL}")
                in_code_block = not in_code_block
            elif in_code_block:
                code_block_lines.append(line)
            else:
                wrapped_lines = textwrap.wrap(line, width=self.terminal_width)
                for wrapped_line in wrapped_lines:
                    print(f"{Fore.WHITE}{wrapped_line}{Style.RESET_ALL}")
        
        # In case the message ends with an unclosed code block
        if code_block_lines:
            print(f"{Fore.BLACK}{Back.WHITE}{' ' * self.terminal_width}")
            for code_line in code_block_lines:
                padded_line = code_line.ljust(self.terminal_width)
                print(f"{Fore.BLACK}{Back.WHITE}{padded_line}{Style.RESET_ALL}")
            print(f"{Fore.BLACK}{Back.WHITE}{' ' * self.terminal_width}{Style.RESET_ALL}")

    def chat(self):
        self._print_welcome_message()

        while True:
            user_input = self.get_multiline_input()

            if self._should_exit(user_input):
                print(f"\n{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
                break

            if self._should_clear_conversation(user_input):
                self.messages.clear()
                print(f"\n{Fore.YELLOW}Conversation cleared. Starting a new chat.{Style.RESET_ALL}")
                continue

            self.messages.append({"role": "user", "content": user_input})

            try:
                response = self._get_claude_response()
                assistant_message = response.content[0].text
                self.messages.append({"role": "assistant", "content": assistant_message})
                self.print_response(assistant_message)
            except Exception as e:
                self._handle_error(e)

    def _print_welcome_message(self):
        welcome_message = """
        Welcome to the Claude Coding Assistant!
        • Type 'exit' or 'quit' to end the chat.
        • Use triple backticks (```) to denote code blocks.
        • Type '/clear' to start a new conversation.
        • Type '###' on a new line to end your input and send it to Claude.
        """
        print(f"{Fore.CYAN}{textwrap.dedent(welcome_message)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'-' * 80}{Style.RESET_ALL}")

    def _should_exit(self, user_input: str) -> bool:
        return user_input.lower().strip() in ["exit", "quit"]

    def _should_clear_conversation(self, user_input: str) -> bool:
        return user_input.lower().strip() == "/clear"

    def _get_claude_response(self):
        return self.client.messages.create(
            model=self.MODEL,
            max_tokens=self.MAX_TOKENS,
            messages=self.messages
        )

    def _handle_error(self, error: Exception):
        print(f"\n{Fore.RED}Error: {str(error)}")
        print(f"{Fore.RED}Failed to get a response from Claude. Please try again.{Style.RESET_ALL}")

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(f"{Fore.RED}Please set the ANTHROPIC_API_KEY environment variable.{Style.RESET_ALL}")
        return
    
    assistant = ClaudeCodingAssistant(api_key)
    assistant.chat()

if __name__ == "__main__":
    main()
