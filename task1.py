import queue
import threading
import time
import random
import sys
import termios
import tty
import os
from helpers.helpers import print_header, print_footer

# Створення черги для заявок
request_queue = queue.Queue()

# Лічильник для унікальних заявок
request_counter = 0
# Флаг для завершення програми
running = True  
# Флаг для генерації заявок
generate_on = True  
# Отримання розміру терміналу
terminal_size = os.get_terminal_size()
terminal_height = terminal_size.lines
terminal_width = terminal_size.columns

def generate_request(request_queue) -> str:
    """Генерує унікальний ідентифікатор заявки та додає його до черги."""
    global request_counter
    current_time_ms = int(time.time() * 1000)  # Поточний час у мілісекундах
    request_counter += 1  # Збільшуємо лічильник
    unique_request_id = f"{current_time_ms}-{request_counter}"
    request_queue.put(unique_request_id)
    return f"{unique_request_id} додано нову заявку до черги."

def process_request(request_queue) -> None:
    """Обробка заявки, якщо черга не порожня"""
    if not request_queue.empty():
        request_id = request_queue.get()
        pass  # Імітація обробки заявки, в ідеалі це має відбуватись в окремому потоці
        return f"{request_id} заявку оброблено."
    else:
        return f"Черга порожня. Заявок для обробки немає."


def clear_line(line_number: int) -> None:
    """Очищує визначений рядок у терміналі"""
    print(f"\033[{line_number};0H", end="")  # Переміщуємо курсор
    print(" " * terminal_width, end="")      # Очищуємо рядок
    print(f"\033[{line_number};0H", end="")  # Повертаємо курсор на початок рядка

def print_status(last_added_request: str) -> None:
    """Функція для виведення інформації внизу термінала"""
    # Очищуємо та виводимо рядок
    clear_line(terminal_height - 4)
    print(
        f"Керування: 'q' - вихід, 'g' - {'вимкнути' if generate_on else 'увімкнути'} генерацію заявок".ljust(
            terminal_size.columns
        )
    )

    # Очищуємо та виводимо рядок
    clear_line(terminal_height - 2)
    print(
        f"Заявок у черзі: {request_queue.qsize()}".ljust(
            terminal_size.columns
        ),
        end="",
        flush=True,
    )
    clear_line(terminal_height - 1)
    print(
        f"Статус: {last_added_request}".ljust(
            terminal_size.columns
        ),
        end="",
        flush=True,
    )

def get_key_press()->str:
    """Чекає на натискання клавіші та повертає її."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # Встановлюємо термінал у режим raw
        tty.setraw(sys.stdin.fileno())  
        # Читаємо один символ
        ch = sys.stdin.read(1)  
    finally:
        # Повертаємо налаштування термінала
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def monitor_keys()->None:
    """Функція для обробки клавіш в окремому потоці"""
    global running
    while running:
        # Обробка натиснених клавіш
        key = get_key_press()
        match key:
            case "q" | "й":
                running = False
            case "g" | "п":
                global generate_on
                generate_on = not generate_on

# Стартовий код програми
if __name__ == "__main__":
    print_header("Імітатція приймання й обробки заявок")
    print("\n\n\n")
    # Створюємо окремий потік для обробки натискань клавіш
    key_thread = threading.Thread(target=monitor_keys, daemon=True)
    key_thread.start()

    try:
        processing_completion_time = 0
        application_time = 0

        # Основний цикл для генерації та обробки заявок
        while running:
            current_time = time.time()

            # Імітація генерації заявок
            if current_time - application_time >= random.uniform(0.5, 1) and generate_on:
                print_status(generate_request(request_queue))
                application_time = current_time

            # Імітація часу на обробку заявок
            if current_time - processing_completion_time >= random.uniform(0.7, 1):
                print_status(process_request(request_queue))
                processing_completion_time  = current_time

    except KeyboardInterrupt:
        running = False
    print()
    print_footer("Програму завершено.")
