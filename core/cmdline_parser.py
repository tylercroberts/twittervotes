from argparse import ArgumentParser

from .app_logger import get_logger


def validated_args(args):

    logger = get_logger()
    unique_hashtags = list(set(args.hashtags))

    if len(unique_hashtags) < len(args.hashtags):
        logger.info(("Some hashtags passed were duplicated and will be ignored"))

        args.hashtags = unique_hashtags

    if len(args.hashtags) > 4:
        logger.error("Voting app only accepts 4 hashtags at a time")

        args.hashtags = args.hashtags[:4]

    return args


def parse_commandline_args():
    argparser = ArgumentParser(
        prog = "twittervoting",
        description="Collect votes using twitter hashtags."
    )
    required = argparser.add_argument_group("required arguments")

    required.add_argument("-ht", "--hashtags",
                          nargs="+", required=True,
                          dest='hashtags',
                          help=("Space separated list specifying the ashtags that will be used for voting. \n"
                                "Type the hashtags without the hash symbol"))

    args = argparser.parse_args()
    return validated_args(args)

