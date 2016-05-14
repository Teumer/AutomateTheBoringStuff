#! python3
import logging

# Comment out if debugging
# logging.disable(logging.DEBUG)

logging.basicConfig(
    filename="program_log.txt",
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Start of program")


def factorial(n):
    """

    :param n:
    :return:
    """
    logging.debug("Start of factorial ({})".format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is {0}, total is {1}".format(i, total))

    logging.debug("End of factorial ({})".format(n))
    return total


print(factorial(5))
logging.debug("End of program")
