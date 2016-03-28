#! coding=utf8
from material.frontend import Module


class AlbumModule(Module):
    order = 7
    icon = "mdi-action-perm-media"
    slug = 'album'

    @property
    def label(self):
        return u"相册"
