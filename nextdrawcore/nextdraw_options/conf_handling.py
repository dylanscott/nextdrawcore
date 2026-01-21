import copy
from importlib import import_module
from types import SimpleNamespace

def get_conf(conf_module):
    """
    input: conf_module, e.g. "nextdrawcore.nextdraw_conf"
    outputs a SimpleNamespace copy of the module.
    it must be a *copy* because otherwise changes made in one
    NextDraw/NextDrawControl/NextDrawMerge instance will be reflected across other instances.
    This comes up in tests and in multi-NextDraw setups.
    """
    params = import_module(conf_module) # Configuration file
    params = SimpleNamespace(**copy.deepcopy(params.__dict__))
    return params # todo, remove dudner methods if time
