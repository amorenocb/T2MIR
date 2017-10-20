import numpy as np


def get_data_dimensions(data_file_name):
    return data_file_name.split("-")[2].split("_")[0].split("x")[1]


def get_data_descriptors(data):
    descriptors = []
    descriptor_dim = get_data_dimensions(data)
    for i in range(0, len(data), descriptor_dim):
        descriptors.append(data[i:i + descriptor_dim])
    return descriptors

class Dataset():

    def __init__(self, q_file, r_file):
        self._q_data = np.fromfile(q_file, np.float32)
        self._r_data = np.fromfile(r_file, np.float32)

        self._q_descriptors = get_data_descriptors(q_file)
        self._r_descriptors = get_data_descriptors(r_file)

    def _get_q(self):
        return self._q_descriptors

    def _get_r(self):
        return self._r_descriptors

    def _set_q(self, new_q_file):
        self._q_descriptors = get_data_descriptors(new_q_file)

    def _set_r(self, new_r_file):
        self._r_descriptors = get_data_descriptors(new_r_file)

    R = property(_get_r, _set_r)
    Q = property(_get_q, _set_q)


