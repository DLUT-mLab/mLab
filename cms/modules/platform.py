#! coding=utf8
from material.frontend import Module


class PlatformModule(Module):
    order = 8
    icon = "mdi-file-cloud-done"
    slug = 'platform'

    @property
    def label(self):
        return u"在线预测平台"
