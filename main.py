from argparse import ArgumentParser

def parse_args(args):
    parser = ArgumentParser(
        'action foreach',
        description='Run action on list of repos.'
    )
    parser.add_argument(
        'repos',
        help="Comma-separated list of repos to run action on.",
        type=str,
    )
    parser.add_argument(
        'action',
        help="Name of action to run for each repo.",
        type=str,
    )
    parser.add_argument(
        '--pat',
        required=False,
        help="Personal access token.",
        type=str,
    )
    return parser.parse_args(args)

def main(args):
    # input parsing
    args = parse_args(args)

    # for each repo
    for repo in args.repos.split(','):
        pass

if __name__ == "__main__":
    main()
