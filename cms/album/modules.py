#! coding=utf8
from material.frontend import Module


class Album(Module):
    order = 9
    icon = "mdi-action-perm-media"

    @property
    def label(self):
        return u"相册"

