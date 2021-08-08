# python-setup

Setup for Python.

## opening in WSL

Once you have installed and activated WSL an Ubuntu terminal will open running a virtual machine on your windows computer.

This is separate from your normal runtime and acts a little like a virtual environment (see below) but with more system access. This allows you to run linux commands instead of dos.

As a result, you may need to mount your C drive or copy data files into WSL to be able to act on them.

You can create a new directory using 

```
mkdir pyannote-audio-tutorial  
```
(you can name this whatever you want)

you can then enter the new directory using 
```
cd pyannote-audio-tutorial
```

copy any files you need into WSL using

```
cp /mnt/c/Users/<your_name>/<path_to_the_file>/filename.type .
```
if you have not yet cloned the git repository, you can do this now. 



alternatively you can copy the files into your present working directory
- for example, to copy the requirements file, use
```
cp /mnt/c/Users/<your_name>/<path_to_the_file>/requirements.txt .
```

## Python and Pip Runtime

To run python you need a python runtime. This is a basically an interpreter for the python language that translates your code into operations.
There are many different ways to setup python. It is not important to understand these in detail, but it is useful to be able to follow what you did and how you did it.

You can find out what version of python you have with

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

When developing it is good practice to isolate the environment that you are working on from the underlying system it is running on.
One simple (but not entirely robust) way of doing this is using virtual environments. These are like isolated sandboxes that think they are all that exists.
They begin as blank slates. You then install libs into them. You can destroy them / recreate them. Most importantly, if anything goes wrong, it only goes wrong in the virtual environment. Not in the underlying controlling system.


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

Once activated, commands using `python` and `pip` will use those related to the virtual env.

You can also use the python binary or related pip binary in this environment with
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

## running Speech Diarization

Once you have activated your virtual environment 
```
. ./.my-virtual-env/bin/activate
```

and run the Makefile

```
make run
```

you should now have installed pyannote-audio and torch via the requirements.txt (see setup.py). Torch is large so this will take a while but you will only need to do this once.

From there, all you need to do is point the diarization pipeline at your data and run.

```
python speechdiarization/main.py --input /Users/<your_name>/<path_to_the_file>/<data directory>
```

The script looks for a directory called 'wavfiles'. It will upload each .wav file in this directory in turn. 
First it processes and outputs the diarization results into a new directory alongside the 'wavfile' directory (called diarization). 
Next the script uses this diarization pipeine to process the overlap data from the conversation.

You can see **https://github.com/pyannote/pyannote-audio** for examples and a comprehensive description of the pyannote-audio pipelines.

## returning to Windows from WSL

When everything is done, depending on how you ran the files, you may need to copy all the output files generated back to Windows from WSL
You can do this using 

```
cp <filename> /mnt/c/Users/<your name>/<path>
```
for a file, or

```
cp <???> /mnt/c/Users/<your name>/<path>
```

for a directory

[comment]: <> ( also helpful: https://linuxhint.com/transfer-files-wsl-windows/)
[comment]: <> (TODO: how to copy a directory from WSL to windows; check all works on WSL; test if works with UoN Onedrive links) 

