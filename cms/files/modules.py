#! coding=utf8
from material.frontend import Module


class Files(Module):
    order = 10
    icon = "mdi-action-work"

    @property
    def label(self):
        return u"平台和资料"

