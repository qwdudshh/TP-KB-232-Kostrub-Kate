import logging

def sum(a, b):
    result = a + b
    logging.info(f"Операція: {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logging.info(f"Операція: {a} - {b} = {result}")
    return result

def mult(a, b):
    result = a * b
    logging.info(f"Операція: {a} * {b} = {result}")
    return result

def div(a, b):
    if b != 0:
        result = a / b
        logging.info(f"Операція: {a} / {b} = {result}")
        return result
    else:
        logging.error("Спроба ділення на нуль!")
        raise ValueError("Ділення на нуль неможливе!")
