#! coding=utf8
from material.frontend import Module


class Member(Module):
    order = 5
    icon = "mdi-action-account-child"

    @property
    def label(self):
        return u"成员介绍"

