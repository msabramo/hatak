class Plugin(object):

    @property
    def config(self):
        return self.app.config

    @property
    def registry(self):
        return self.config.registry

    @property
    def settings(self):
        return self.app.settings

    def init(self, app):
        self.app = app
        self.validate_plugin()

    def make_config_include_if_able(self):
        try:
            self.config.include(self.get_include_name())
        except NotImplementedError:
            pass

    def get_include_name(self):
        raise NotImplementedError()

    def add_to_registry(self):
        pass

    def before_config(self):
        pass

    def after_config(self):
        pass

    def add_unpackers(self, unpacker):
        pass

    def add_controller_plugins(self, plugins):
        pass

    def add_commands(self, parent):
        pass

    def validate_plugin(self):
        pass


def reify(method):
    """Decorator for making reify methods with request instance for request."""

    def requester(self, request):
        def on_request(*args, **kwargs):
            return method(self, request, *args, **kwargs)
        return on_request
    return requester