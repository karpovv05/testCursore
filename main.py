import logging

logging.basicConfig(level=logging.INFO)

for i in range(3):
    logging.info(f"Начало внешнего цикла: {i}")
    for j in range(2):
        logging.info(f"  Внутренний цикл: {j}")
        print(f"Внешний цикл: {i}, Внутренний цикл: {j}")
    logging.info(f"Конец внешнего цикла: {i}")