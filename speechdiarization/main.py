import sys

import pyannote
import speechdiarization.diarization


def main():
    data_dir = '/Users/bryonybuck/data/HSSS/e187_22346_31546'
    return speechdiarization.diarization.run_diarization_pipeline(
        data_dir, output_dir=None, overwrite_data=False
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())

