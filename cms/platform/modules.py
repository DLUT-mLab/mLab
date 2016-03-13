#! coding=utf8
from material.frontend import Module


class Platform(Module):
    order = 9
    icon = "mdi-file-cloud-done"

    @property
    def label(self):
        return u"在线预测平台"

