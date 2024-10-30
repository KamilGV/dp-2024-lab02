from threading import Thread
from datetime import datetime
from pathlib import Path
import random
import os
import time

from faker import Faker

from src.logger import Logger
from src.enums import Level
from src.formatters import InitialCaseFormatter, UpperCaseFormatter
from src.writers import ConsoleWriter, FileWriter


fake = Faker()

path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(path, '../../dp-2024-lab02'))
base_path = Path(parent_path)
folder_path = base_path / "logs"

time_str = datetime.now().strftime("%yyyy-%m-%d-%H-%M-%S")
file_name = f"DP.P2.{time_str}.log"
file_path = folder_path / file_name

upper_formatter = UpperCaseFormatter()
initial_formatter = InitialCaseFormatter()

console_writer = ConsoleWriter()
file_writer = FileWriter(file_path=file_path)
print(file_path)



def thread_func():
    """
    Создаёт в нескольких потоках логгеры и записывает в них сообщения

    :return None
    """
    for i in range(3):
        logger = Logger(formatter=random.choice([initial_formatter, upper_formatter]),
                        writer=random.choice([file_writer, console_writer]))

        message = fake.text(max_nb_chars=20)
        level = random.choice(list(Level))

        logger.log(message, level)
        time.sleep(random.randrange(0, 2))


if __name__ == "__main__":
    threads = []
    for _ in range(10):
        thread = Thread(target=thread_func, args=())
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


