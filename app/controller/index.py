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
    if 'path' in request.params:
        path = os.path.normpath(os.path.join(
            request.app.root_dir,
            '../../../write/md-blog',
            request.params['path']
        ))
    else:
        path = os.path.normpath(os.path.join(
            request.app.root_dir,
            request.params['inner_path']
        ))

    buffer = io.BytesIO()
    markdown.markdownFromFile(path, buffer)

    title = ''
    with open(path, 'r', encoding='utf-8') as f:
        title = f.readline()[2:-1]

    return {
        'title': title,
        'markdown_content': buffer.getvalue().decode('utf-8')
    }


def about(request):
    request.params.update({
        'inner_path': 'frontend/markdown/about.md'
    })

    return article(request)
