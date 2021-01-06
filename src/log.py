import logging

logging.basicConfig(filename='../error.log', format='[%(levelname)s]-%(asctime)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def Spam(user, nameCommand):
    logging.warning(f"{user} is spamming {nameCommand}")
