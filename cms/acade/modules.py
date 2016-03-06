#! coding=utf8
from material.frontend import Module


class Acade(Module):
    order = 3
    icon = "mdi-action-pageview"

    @property
    def label(self):
        return u"学术研究"

