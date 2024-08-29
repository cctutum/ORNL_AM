import h5py
import os

downloads_path = os.path.expanduser('~/Downloads')
file = '2021-07-13 TCR Phase 1 Build 1.hdf5'
path_file = os.path.join(downloads_path, file)

build = h5py.File(path_file, 'r')
print(list(build.keys()))


def print_structure(name, obj):
    print(name)
    if isinstance(obj, h5py.Dataset):
        print(f"  Shape: {obj.shape}, Dtype: {obj.dtype}")
        
build.visititems(print_structure)