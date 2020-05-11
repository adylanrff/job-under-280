import argparse


def get_arguments():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--scrap_job", help="Scrap jobs from the database", action='store_true')
    argparser.add_argument("--tweet", help="Scrap jobs from the database", action='store_true')

    return argparser.parse_args()

