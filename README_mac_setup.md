## Python Runtime

To run python you need a python runtime. This is an interpreter for the python language that translates your code into a real operations.
There are many different ways to setup python on your machine.

to start off, find out what version of python you have with

```
python --version
```

you can also find out some information about where python runtime is located with

```
which python
```

This will help you identify which python you are currently using.

### System python (not recommended)

you'll find that mac comes with a pre-shipped version of python. Generally this gets in the way and it is best to ignore it.


### pyenv (not recommended)

pyenv is good but a little restrictive and hasn't really developed into industry standard. It has a few problems with how it sets up virtual environments. It uses the base system python as a python runtime and then builds virtual envs ontop of them (not the best)

#### Setup
I can write more here ont his if you want but I don't think you need it - let me know if you're having problems
````
# install
brew install pyenv

# add config to zsh (If you don't use zsh , get it and do)
echo '
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
fi
' >> ~/.zshrc

# install zlib
brew update
brew upgrade
brew install zlib
export CFLAGS="-I$(brew --prefix openssl)/include -I$(xcrun --show-sdk-path)/usr/include"
export LDFLAGS="-L$(brew --prefix openssl)/lib"

# set python 3.6.8 as default
pyenv install 3.6.8
pyenv global 3.6.8

# update config in current terminal
exec $SHELL

# this should display v3.6.8
python --version
````


### Conda / Anaconda
This is a product built by continuum and is kinda cool. It has some problems as well and can be quite large if you opt for the full anacaconda installation.
* Anaconda: The full python runtime + loads of pre built ananconda specific versions of python libs. It also comes with a lot of packages you don't need and can be an issue when you want portability and sharable/ recreatable environments
* miniconda: you can get the basic python runtime with this and only use what you need (This is my recommendation. I use this solution!).

#### Setup

Get the conda setup here
```
https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
```

run the installer
```
bash Miniconda3-latest-MacOSX-x86_64.sh -b -p $HOME/miniconda
conda init
```

you can create new python installtions with the following (say this will create python 3.6 runtime)
```
conda create -n python3.6 python=3.6 -c conda-forge
conda install -n python3.6 virtualenv
python --version
```



## Virtual environments

As we mentioned before, when developing its good to isolate the environment you are working on from the underlying system its running on.
one way of doing this is using virtual environments. These are like little isolated sandboxes that think they are all that exists.
They start as blank slates and you install libs into them. You can destroy them / recreate them and alter them to how you want them.

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
