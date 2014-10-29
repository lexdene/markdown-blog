import os
import hbml

import drape


class HelperWrapper:
    def __init__(self, request, path):
        self.__request = request
        self.__path = path

    def include_style(self, path=None):
        if path is None:
            path = self.__path

        path = 'css/%s.css' % path
        resource_info = self._get_resource_info(path)

        return hbml.compile(
            '%link(href=path, rel="stylesheet", type="text/css")/',
            dict(
                path='%s?v=%s' % (
                    resource_info[0], resource_info[1]
                )
            )
        )

    def include_script(self, path=None):
        if path is None:
            path = self.__path

        if drape.config.config.FRONTEND_DEBUG:
            path = 'js/%s.js' % path
        else:
            path = 'js/%s.min.js' % path

        resource_info = self._get_resource_info(path)

        return hbml.compile(
            '%script(src=path)',
            dict(
                path='%s?v=%s' % (
                    resource_info[0], resource_info[1]
                )
            )
        )

    def include_lib_script(self, path):
        return hbml.compile(
            '%script(src=path)',
            dict(
                path=os.path.join(
                    drape.config.config.LIB_ROOT,
                    path
                )
            )
        )

    def path_to(self, path):
        return os.path.join(
            '/',
            self.__request.root_path(),
            path
        )

    def _get_resource_info(self, path):
        'return a (url, version_tag, path) tuple'
        url = os.path.join(
            '/',
            self.__request.root_path(),
            drape.config.config.RESOURCE_URL_ROOT,
            path
        )
        file_path = os.path.join(
            self.__request.app.root_dir,
            drape.config.config.RESOURCE_PATH_ROOT,
            path
        )
        version_tag = os.path.getmtime(file_path)

        return (url, version_tag, file_path)

    def _helpers(self):
        return [
            (attr_name, getattr(self, attr_name))
            for attr_name in dir(self)
            if attr_name[0] != '_'
        ]


def default_frame(func):
    prefix = 'app.controller.'
    assert prefix == func.__module__[:len(prefix)]

    controller_path = '%s/%s' % (
        func.__module__[len(prefix):],
        func.__name__
    )

    def controller_func(request):
        var_dict = func(request)

        helper = HelperWrapper(request, controller_path)
        var_dict.update(helper._helpers())

        return drape.response.Response(
            hbml.compile_file(
                os.path.normpath(
                    os.path.join(
                        request.app.root_dir,
                        'frontend/templates',
                        controller_path + '.hbml'
                    )
                ),
                var_dict
            )
        )

    return controller_func
