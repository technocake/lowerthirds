from django.template.loader import render_to_string
from cairosvg import svg2png
import shutil
import os
import random
import string
from django.conf import settings


def export_graphics(event):
    dir_name, files = render_all_lowerthirds_to_png(event)
    zipfile = create_zip(dir_name)
    return zipfile


def render_all_lowerthirds_to_png(event):
    path = settings.RENDER_DIR + '/' +  ''.join(random.choice(string.ascii_lowercase) for i in range(12))  # noqa
    if not os.path.exists(path):
        os.makedirs(path)

    files = []
    for lowerthird in event.lowerthirds.all():
        files.append(render_lowerthird_to_png(lowerthird, path))

    return (path, files)


def render_lowerthird_to_png(lowerthird, path):
    data = {
        'name': lowerthird.name,
        'title': lowerthird.title,
        'path': path,
    }
    svg = render_to_string('lowerthird.svg', data)
    filename = '{path}/{name}_{title}.png'.format(**data)
    svg2png(bytestring=svg, write_to=filename)  # noqa

    return filename


def create_zip(dir_path):
    zipfile = ''.join(random.choice(string.ascii_lowercase) for i in range(12))  # noqa
    path = '{}/{}'.format(settings.RENDER_DIR, zipfile)
    shutil.make_archive(path, 'zip', dir_path)

    return path + '.zip'


def zipfile_to_bytes(zipfile):
    with open(zipfile, 'rb') as f:
        return f.read()
