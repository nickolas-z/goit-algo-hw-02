from collections import deque
from colorama import Style, init, Fore
from helpers import Application, print_execution_time


class Task1(Application):
    """
    Application class
    """

    def is_symmetric(self, expression: str) -> str:
        """Перевіряє чи є дужки в рядку симетричними"""
        stack = []
        matching_brackets = {")": "(", "]": "[", "}": "{"}

        for char in expression:
            if char in matching_brackets.values():  # Якщо відкриваюча дужка
                stack.append(char)
            elif char in matching_brackets:  # Якщо закриваюча дужка
                if not stack or stack.pop() != matching_brackets[char]:
                    return False

        return True if not stack else False

    @print_execution_time
    def run(self):
        init(autoreset=True)
        print(f"{Style.BRIGHT}{Fore.CYAN}Приклад очікуваного результату:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}")
        print("( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично\n( 23 ( 2 - 3);: Несиметрично\n( 11 }: Несиметрично")
        print(f"{Style.RESET_ALL}")
        while True:
            user_input = input("Введіть рядок для перевірки ('q' - вихід): ")
            if user_input in ["q", "й", "Q", "Й"]:
                break
            is_s = self.is_symmetric(user_input)
            print(
                f"Розділювачі {Style.BRIGHT}{Fore.GREEN if is_s else Fore.RED}{'симетричні' if is_s else 'несиметричні'}{Style.RESET_ALL}. Кількість символів (всього): {len(user_input)}"
            )


# Run the application
if __name__ == "__main__":
    try:
        Task1("Symmetry estimator!").run()
    except EOFError:
        print(f"\n{Fore.RED}Input ended unexpectedly. Exiting the application.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled (Ctrl+C). Exiting the application.")
