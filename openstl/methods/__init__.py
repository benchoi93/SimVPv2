# Copyright (c) CAIRI AI Lab. All rights reserved

from .convlstm import ConvLSTM
from .crevnet import CrevNet
from .e3dlstm import E3DLSTM
from .mau import MAU
from .mim import MIM
from .phydnet import PhyDNet
from .prednet import PredNet
from .predrnn import PredRNN
from .predrnnpp import PredRNNpp
from .predrnnv2 import PredRNNv2
from .simvp import SimVP
from .tau import TAU
from .dmvfn import DMVFN
from .dynmix import better_loss, covariance

method_maps = {
    'convlstm': ConvLSTM,
    'crevnet': CrevNet,
    'e3dlstm': E3DLSTM,
    'mau': MAU,
    'mim': MIM,
    'phydnet': PhyDNet,
    'prednet': PredNet,
    'predrnn': PredRNN,
    'predrnnpp': PredRNNpp,
    'predrnnv2': PredRNNv2,
    'simvp': SimVP,
    'tau': TAU,
    'dmvfn': DMVFN,
    "dynmix": better_loss
}

__all__ = [
    'method_maps', 'ConvLSTM', 'CrevNet', 'E3DLSTM', 'MAU', 'MIM',
    'PredRNN', 'PredRNNpp', 'PredRNNv2', 'PhyDNet', 'PredNet', 'SimVP',
    'TAU', "better_loss", "covariance"
]
