conda install -c conda-forge pybind11

mkdir intel-qs/build
cd intel-qs/build
CXX=g++ cmake -DIqsPython=ON -DIqsNative=ON -DBuildInterface=ON ..
make