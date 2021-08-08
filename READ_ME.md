# python-setup

Setup for Python.

## examples with makefile

We've added a Makefile so that you can have a see what each command does individually.

To run each example in the Makefile just execute

```
make <name of task>
e.g.
make piplist
```
To run all commands execute

```
make run
```

## Python and Pip Runtime

To runn python you need a python runtime. This is a basically an interpreter for the python language that translates you code into a actual operations.
You don't really need to know anything about this. But what is inportant is understanding that there are many different ways to setup python 
on your machine.

find out what version of python you have with

```
python --version
```

you can find out which pip version you are running using

```
pip3 --version
```

you can also find out some information about where python runtime is located with 

```
which python
```

This will help you identify which python you are currently using.

You should be running around python 3.8 and pip 20. 

## Virtual environments

When developing its good to isolate the environment you are working on from the underlying system its running on.
one simple ( but not entirely robust) way of doing this is using virtua environments. Think of these are little isolated sandboxes that think they are all that exists.
The start as blank slates. You install libs into them. You can destroy them / recreate them. Just get used to them.

To create a virtual env you can use the `venv` module in the base python, and define the `directory` in which to create this venv,

```
python -m venv .my-virtual-env
```
This will create a hidden directory called `.my-virtual-env` in the current directory. 

### Activate the environment

You can activate this venv here by sourcing the activate file
```
. ./.my-virtual-env/bin/activate
```

once activated using `python` and `pip` will use those related to the virtual env.

You can also  just use the python binary or related pip binary in this environment with
```
./.my-virtual-env/bin/python
```
or
```
./.my-virtual-env/bin/pip
```

Make sure you are not in an activated virtual environment by executing `deactivate` and checkout what happens if you execute 
```
./.my-virtual-env/bin/pip list
```
versus
```
pip list
```

You should see the difference in the libraries installed in virtual env verses those installed in the global python runtime environment.

## Processing Speech Diarization

Once you have activated your virtual environment and run the Makefile, 

```
. ./.my-virtual-env/bin/activate

make run
```

you should have installed pyannote-audio and torch via the requirements.txt (see setup.py). Torch is large so this will take a while but you will only need to do this once.

From there, all you need to do is point the diarization pipeline at your data and run.

```
python speechdiarization/main.py --input /Users/<your_name>/<path_to_the_file>/<data directory>
```

The script looks for a directory called 'wavfiles'. It will upload each .wav file in this directory in turn. 
First it processes and outputs the diarization results into a new directory alongside the 'wavfile' directory (called diarization). 
Next the script uses this diarization pipeine to process the overlap data from the conversation.

You can see **github and **colab for examples and comprehensive description of the pyannote-audio pipelines.


