from colorama import Style, init, Fore
from helpers import Application, print_execution_time


class Task1(Application):
    """
    Application class
    """

    @print_execution_time
    def run(self):
        init(autoreset=True)

        while True:
            user_input = input("Enter a command: ")
            if user_input == "exit":
                break   


# Run the application
if __name__ == "__main__":
    try:
        Task1("Welcome to the application processing!").run()
    except EOFError:
        print(f"\n{Fore.RED}Input ended unexpectedly. Exiting the application.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled (Ctrl+C). Exiting the application.")
