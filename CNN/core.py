import torch
import torch.nn as nn
import logging
from .utils import MODEL_URLS
import os


class BaseCNN(nn.Module):
    NAME = "Base"

    def __init__(self, depth: int, pretrain: bool = False, train: bool = False) -> None:
        super(BaseCNN, self).__init__()
        self.depth = depth
        self.pretrain = pretrain
        self.train = train
        self.input_channel = 3

    def forward(self, x):
        raise

    def build_model(self):
        raise

    def load_state_dict_(self, drop_key_lens: int = None,
                         fine_tuning: bool = True):
        """
        arg:
            drop_key_lens:int , how many layer you want drop.
                example :  static_key = {'layer1.weight':1,
                                        'layer1.bias':2,
                                        'layer2.weight':1,
                                        'layer2.bias':0}
                            if drop_key_lens = 1, we will drop 'layer2.weight' and 'layer2.bias'
            fine_tuning : bool , is keep base layer's
        """
        from torch.hub import load_state_dict_from_url
        url = MODEL_URLS[self.NAME][str(self.depth)]
        model_dir = os.path.join(os.path.abspath(".."), "model_params")
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        if os.path.isfile(os.path.join(model_dir, url.split("/")[-1])):
            static = torch.load(os.path.join(model_dir, url.split("/")[-1]))
        else:
            static = load_state_dict_from_url(url=url, model_dir=model_dir)
        if drop_key_lens is not None:
            drop_key = list(static.keys())[-drop_key_lens * 2:]
            for i in drop_key:
                static.pop(i)
        self.load_state_dict(state_dict=static, strict=False)
        if fine_tuning:
            if drop_key_lens is None:
                raise ValueError("you can't fine_tuning while you don't want to drop anything")
            all_lens = sum(1 for i in self.named_parameters())
            for k, v in enumerate(self.parameters()):
                if k < all_lens - drop_key_lens * 2:
                    v.requires_grad = False
