#! coding=utf8
from material.frontend import Module


class NewsModule(Module):
    """
    asdjflajsldkjf
    """
    order = 2
    icon = "mdi-action-assignment"
    slug = 'news'

    @property
    def label(self):
        return u"新闻动态"

