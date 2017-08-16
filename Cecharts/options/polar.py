# -*- utf-8 -*-

from decorators import check_args

from .base_option import BaseOption
from .tooltip import ToolTip

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Polar(BaseOption):
    def __init__(self):
        self.zlevel = None
        self.z = None
        self.center = None
        self.radius = None
        self.tooltip = ToolTip()

    @check_args
    def set_keys(self, z_level: int=None, z: int=None, center: list=None, radius: list=None):
        self.zlevel = z_level
        self.z = z
        self.center = center
        self.radius = radius
