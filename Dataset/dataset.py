# coding=utf-8
from torch.utils.data import Dataset
import lmdb
import other
import json
import numpy as np


class LmdbDataset(Dataset):
    def __init__(self, root, transformer=None):
        self.env = lmdb.open(root, max_readers=1, readonly=True, lock=False, readahead=False, meminit=False)
        if not self.env:
            print("Cannot create lmdb from root {0}.".format(root))
        with self.env.begin(write=False) as e:
            self.data_num = int(e.get('num'.encode()))
        self.transformer = transformer

    def __len__(self):
        return self.data_num

    def __getitem__(self, index):
        assert index <= len(self), 'Index out of range.'
        # index += 1
        with self.env.begin(write=False) as e:
            img_key = 'image-%09d' % index
            img_base64 = e.get(img_key.encode())
            img = other.base642np_image(img_base64)
            img = img - np.float32([102.9801, 115.9465, 122.7717])
            gt_key = 'gt-%09d' % index
            gt = e.get(gt_key.encode())
            gt = json.loads(gt)
        return img, gt
