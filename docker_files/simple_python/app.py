# Description: A simple python script that prints "Hello, Docker!" to the console.
from loguru import logger

def main():
    logger.info("Hello, Docker!")

if __name__ == "__main__":
    main()