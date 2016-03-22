#! coding=utf8
from material.frontend import Module


class FilesModule(Module):
    order = 10
    icon = "mdi-action-work"
    slug = 'files'

    @property
    def label(self):
        return u"资料下载"

