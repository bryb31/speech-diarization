import os

import torch
from pyannote.database.util import load_rttm


def run_diarization_pipeline(data_dir, output_dir=None, overwrite_data=False):

    # Load dia type pyannote-audio pipeline via pytorch
    model_type = 'pyannote/pyannote-audio'
    pipeline_type = 'dia'
    pipeline = torch.hub.load(model_type, pipeline_type)

    # Input file
    # TODO: find filename from data_dir (os.walk)
    wav_dir = os.path.join(data_dir, "wavfiles")  # e.g./data/wavfiles
    if output_dir is None:
        output_dir = os.path.join(data_dir, "diarization")

    if os.path.exists(output_dir) and not overwrite_data:
        print("Exiting: Output dir already exists. {}".format(output_dir))
        return 1

    for input_file in os.listdir(wav_dir):
        # fixme: avfiles cannot contian dir. make this code handle nested dirs (tip: os.walk + check if item is file)
        file_name, file_extension = input_file.split(".")  # canot handle cases where foo.bar.wav
        input_file_path = os.path.join(wav_dir, input_file)
        print("Currently processing for: {}".format(input_file_path))

        input_file_dict = input_file_dict = {
           'audio': input_file_path
           }

        # Get annotation from pipeline
        annotation = pipeline(input_file_dict)

        # We Write the annotation to file

        output_file_name = "{}.rttm".format(file_name)
        output_file_path = os.path.join(output_dir, output_file_name)

        with open(output_file_path, 'w') as file:
            annotation.write_rttm(file)
        # Load annotation again - im not sure what the load_rttm method returns.
        # will have to check
        loaded_object = load_rttm(output_file_path)

    return 0