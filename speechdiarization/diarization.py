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

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for input_file in os.listdir(wav_dir):
        # fixme: avfiles cannot contain dir. make this code handle nested dirs (tip: os.walk + check if item is file)
        file_name, file_extension = input_file.split(".")  # canot handle cases where foo.bar.wav
        input_file_path = os.path.join(wav_dir, input_file)

        input_file_dict = input_file_dict = {
            'audio': input_file_path
        }
        output_file_name = "{}.rttm".format(file_name)
        output_file_path = os.path.join(output_dir, output_file_name)

        if os.path.exists(output_file_path) and not overwrite_data:
            print("Output path already exists {}".format(
                input_file_path
            ))
            prediction = load_diarization(output_file_path)
        else:
            print("Currently processing for: {}".format(input_file_path))

            # Get prediction from pipeline
            prediction = pipeline(input_file_dict)

            # We Write the prediction to file

            with open(output_file_path, 'w') as file:
                prediction.write_rttm(file)

        overlap_dir = os.path.join(output_dir, 'overlap')
        overlap_file_path = os.path.join(overlap_dir, file_name)

        if os.path.exists(overlap_file_path) and not overwrite_data:
            print("already exist: {}".format(overlap_file_path))
            pass
        else:
            prediction = infer_speaker_overlap_from_audio(
                input_file_dict=input_file_dict,
                output_dir=overlap_dir,
                file_name=file_name
            )

        overlap_prediction = load_diarization(overlap_file_path)
    return 0


def load_diarization(file_path):
    print("Loading Diarization: {}".format(file_path))
    # Load diarization again - im not sure what the load_rttm method returns.
    # will have to check
    diarization = load_rttm(file_path)
    return diarization


def infer_speaker_overlap_from_audio(input_file_dict, output_dir, file_name):
    """
    takes a wav file and runs inferences via model on audio to determine overlap
    writes overlap prediction to output_file_path
    :return:
    """
    model = torch.hub.load('pyannote/pyannote-audio', 'ovl_ami', pipeline=True)
    prediction = model(input_file_dict)

    output_file_path = os.path.join(output_dir, file_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file_path, 'w') as file:
        # TODO: make filenames understandable at a glance. regardless of directory.
        prediction.write_rttm(file)

    return prediction
