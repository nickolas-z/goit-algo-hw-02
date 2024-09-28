import queue
import threading
import time
import random
import sys
import os

# Створення черги для заявок
request_queue = queue.Queue()

# Лічильник для унікальних заявок
request_counter = 0
running = True  # Флаг для завершення програми

# Отримання розміру терміналу
terminal_size = os.get_terminal_size()
terminal_height = terminal_size.lines
terminal_width = terminal_size.columns


# Функція для генерації унікального номера заявки
def generate_unique_request_id():
    global request_counter
    current_time_ms = int(time.time() * 1000)  # Поточний час у мілісекундах
    request_counter += 1  # Збільшуємо лічильник
    return f"{current_time_ms}-{request_counter}"


# Функція для обробки клавіш в окремому потоці
def monitor_keys():
    global running
    while running:
        if sys.stdin.read(1) == "q":  # Перевіряємо, чи натиснута клавіша 'q'
            running = False  # Зупиняємо основний цикл


# Функція для виведення тексту внизу термінала
def print_at_bottom(message):
    # Очищаємо екран
    print("\033[2J", end="")
    # Переміщуємо курсор в нижню частину екрана
    print(f"\033[{terminal_height};0H", end="")
    # Виводимо повідомлення
    print(message, end="", flush=True)


# Стартовий код програми
if __name__ == "__main__":
    # Створюємо окремий потік для обробки натискань клавіш
    key_thread = threading.Thread(target=monitor_keys, daemon=True)
    key_thread.start()

    try:
        while running:
            # Генеруємо нову заявку
            unique_request_id = generate_unique_request_id()
            request_queue.put(unique_request_id)
            print_at_bottom(
                f"Нова заявка: {unique_request_id} додана до черги. Зараз у черзі: {request_queue.qsize()} заявок."
            )

            # Імітація часу на обробку заявок
            time.sleep(random.uniform(0.5, 2))

            # Обробка заявки, якщо черга не порожня
            if not request_queue.empty():
                request_id = request_queue.get()
                print_at_bottom(
                    f"Обробляємо заявку: {request_id}. Заявок у черзі перед обробкою: {request_queue.qsize()}."
                )
                time.sleep(3)  # Імітація часу на обробку заявки
                print_at_bottom(
                    f"Заявку {request_id} оброблено. Залишилося заявок у черзі: {request_queue.qsize()}."
                )

    except KeyboardInterrupt:
        pass
    finally:
        running = False
        print("\nПрограма завершена.")
