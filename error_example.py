#! python3
import traceback


def spam():
    """

    :return:
    """
    bacon()


def bacon():
    """

    :return:
    """
    raise Exception("This is an error message")


try:
    spam()
except:
    error_file = open("error_info.txt", "w")
    error_file.write(traceback.format_exc())
    error_file.close()
    print("The traceback info was written to error_info.txt.")
