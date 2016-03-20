#! coding=utf8
from material.frontend import Module


class Report(Module):
    order = 5
    icon = "mdi-action-description"

    @property
    def label(self):
        return u"学术报告"

