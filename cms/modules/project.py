#! coding=utf8
from material.frontend import Module


class Project(Module):
    order = 4
    icon = "mdi-action-work"

    @property
    def label(self):
        return u'科研项目'

