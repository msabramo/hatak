from hatak.plugins import Plugin
from hatak.plugins.sql import SqlPlugin

from .commands import AlembicCommand


class AlembicPlugin(Plugin):

    def add_commands(self, parent):
        parent.add_command(AlembicCommand())

    def add_depedency_plugins(self):
        self.app._validate_dependency_plugin(SqlPlugin)
