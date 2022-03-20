# Building From Source

The recommended build-from-source method is to use pip packaging. If, however, you're running into issues, you can manually build intel-qs using Anaconda and deal with module sorcery yourself.

## Unix

The general flow for Unix is to make sure you have `python-dev`(aka `python-devel`), `make` and `g++`. This is, of course, in addition to `python` and `pip`, which you hopefully already have. Keep in mind some of these tools may come pre-bundled with others. If in doubt, `which make`, `which g++`, etc. to verify.

Below are verified-correct setups to builds from source of the pip package. Once you've done the "prep", you should be able to just run `pip install .` in this folder and build/install the package. You also need `cmake` and `pybind11` to build `intel-qs` but they should be pulled by `pip` tooling automatically.

### CentOS 8
```bash
# You can skip git/python/pip setup if you have all of them
sudo yum install git
sudo yum install python3
curl https://bootstrap.pypa.io/pip/3.6/get-pip.py > get-pip.py
python3 get-pip.py

sudo yum install make
sudo yum install platform-python-devel.x86_64

pip install .
```

## Build `intel-qs` manually

Building manually is probably something you should only try if pip is giving you trouble (and you should report that on GitHub Issues). You will need to install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) to proceed. Verify successful installation by checking that `which python` returns an anaconda path prior to attempting any `intel-qs` setup.

If you're on Unix (including OS X), you should be able to get going by running [`manual-setup.sh`](./manual-setup.sh) and waiting a while. If you're on Windows, you can still do that by using [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) (highly recommended).

The end result of running [`manual-setup.sh`](./manual-setup.sh) is that you (hopefully) now have `intel-qs` built from the Python/C++ source. However, the qublets package is not connected anywhere, since you didn't use `pip`. You can copy the contents of `intel-qs/build/lib` and `qublets` (preserving the folder structure) anywhere you'd like to have the `qublets` module accessible and handle module dependencies manually.