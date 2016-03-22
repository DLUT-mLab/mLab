#! coding=utf8
from material.frontend import Module


class ProjectModule(Module):
    order = 4
    icon = "mdi-action-work"
    slug = 'project'

    @property
    def label(self):
        return u'科研项目'

