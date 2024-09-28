from collections import deque
from colorama import Style, init, Fore
from helpers import Application, print_execution_time


class Task1(Application):
    """
    Application class
    """

    def is_palindrome(self, s: str) -> bool:
        """ Перевіряє чи є рядок паліндромом """
        # Нормалізація рядка: переведення в нижній регістр і видалення пробілів
        normalized_str = "".join(char.lower() for char in s if char.isalnum() and char not in "-,.'!?\"")

        # Створюємо двосторонню чергу з символів рядка
        char_deque = deque(normalized_str)

        # Порівнюємо символи з початку і кінця
        while len(char_deque) > 1:
            if char_deque.popleft() != char_deque.pop():
                return False

        return True

    @print_execution_time
    def run(self):
        init(autoreset=True)
        print(f"{Style.BRIGHT}{Fore.CYAN}Приклади паліндромів:{Style.RESET_ALL}")
        print(f"""{Fore.YELLOW}
            Уму – мінімуму!
            І розморозь зором зорі
            Ущипне — та шатен: пищу!
            А результатів? Вітать лузера!
            А баба на волі — цілована баба.
            Три психи пили Пилипихи спирт.
                {Style.RESET_ALL}""")
        while True:
            user_input = input("Введіть фразу для перевірки ('q' - вихід): ")
            if user_input in ["q", "й", "Q", "Й"]:
                break
            is_p=self.is_palindrome(user_input)
            print(
                f"Це {Style.BRIGHT}{Fore.GREEN if is_p else Fore.RED}{'паліндром' if is_p else 'не паліндром'}{Style.RESET_ALL}. Кількість символів (всього): {len(user_input)}"
            )


# Run the application
if __name__ == "__main__":
    try:
        Task1("Palindrome finder!").run()
    except EOFError:
        print(f"\n{Fore.RED}Input ended unexpectedly. Exiting the application.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled (Ctrl+C). Exiting the application.")
