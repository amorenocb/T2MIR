import numpy as np


def get_data_dimensions(data_file):
    return int(data_file.split("-")[2].split("_")[0].split("x")[1])


def get_data_descriptors(data_file):
    data = np.fromfile(data_file, np.float32)
    descriptor_dim = get_data_dimensions(data_file)

    descriptors = []
    for i in range(0, len(data), descriptor_dim):
        descriptors.append(data[i:i + descriptor_dim])
    return np.array(descriptors, dtype=np.float32)

class Dataset():

    def __init__(self, data_file):
        self._data_descriptors = get_data_descriptors(data_file)

    def _get_descriptors(self):
        return self._data_descriptors

    def _set_data(self, new_data_file):
        self._data_descriptors = get_data_descriptors(new_data_file)

    descriptors = property(_get_descriptors, _set_data)


