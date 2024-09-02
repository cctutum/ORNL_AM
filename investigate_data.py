import h5py
import os

downloads_path = os.path.expanduser('~/Downloads')
file = '2021-07-13 TCR Phase 1 Build 1.hdf5'
path_file = os.path.join(downloads_path, file)

build = h5py.File(path_file, 'r')
print(f"\nFile name: {file}")
print(list(build.keys()), '\n')


def preview_hdf5(name, obj):
	if isinstance(obj, h5py.Group):
		print(f"Group: {name}")
	elif isinstance(obj, h5py.Dataset):
		print(f"Dataset: {name}")
		print(f"Shape: {obj.shape}, Dtype: {obj.dtype}")

# with h5py.File(path_file, 'r') as f:
# 	f.visititems(preview_hdf5)

build.visititems(preview_hdf5)