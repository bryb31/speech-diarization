import sys
import argparse


import speechdiarization.diarization


def get_parser():
    parser = argparse.ArgumentParser(description='Speech Diarization')
    parser.add_argument(
        '--input',
        help="input directory",
        default='/Users/bryonybuck/data/HSSS/e187_22346_31546'
    )
    return parser


def main(args=None):

    parser = get_parser()
    args = parser.parse_args()

    print(args.input)

    data_dir = args.input
    speechdiarization.diarization.run_diarization_pipeline(
        data_dir, output_dir=None, overwrite_data=False
    )

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())    # add new line at end
