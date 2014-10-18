import os
import io
import markdown

import drape

from . import frame


def index(request):
    return drape.response.Response(
        'hello'
    )


@frame.default_frame
def article(request):
    path = request.params['path']

    buffer = io.BytesIO()

    markdown.markdownFromFile(
        os.path.normpath(os.path.join(
            request.app.root_dir,
            '../../write/md-blog',
            path + '.md'
        )),
        buffer
    )

    return {
        'markdown_content': buffer.getvalue().decode('utf-8')
    }
    return drape.response.Response(
        'hello:<br />%s<br />%s' % (
            path,
            buffer.getvalue().decode("utf-8")
        )
    )
