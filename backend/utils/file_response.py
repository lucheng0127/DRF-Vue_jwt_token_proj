#-*- coding: utf-8 -*-
import os, zipfile

from django.http import HttpResponse
from django.utils.encoding import escape_uri_path

def file_response(file_path='/dev/null', filename=u''):
    if os.path.exists(file_path):
        # 返回file
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path(filename))
            return response

    return False

def file_pack(file_path='', output_filename=''):
    '''
    :param file_path:文件夹路径
    :param output_path:
    :return: 压缩file_path 目录下的文件并放置与output_path目录下
    '''
    if os.path.isdir(file_path):
        files = os.listdir(file_path)
        if output_filename == '':
            output_filename = os.path.join(file_path, 'data.zip')
        zip_file = zipfile.ZipFile(output_filename, 'w')
        for file in files:
            path_file = os.path.join(file_path, file)
            zip_file.write(path_file, file)
        zip_file.close()
        return True
