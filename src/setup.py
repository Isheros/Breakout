#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
from cx_Freeze import setup, Executable

# Modulos Excluidos
exclude_modules=[
    'email','AppKit','Foundation','bdb',
    'difflib','tcl','Tkinter','Tkconstants',
    'curses','distutils','setuptools','urllib',
    'urllib2','urlparse','BaseHTTPServer','_LWPCookieJar',
    '_MozillaCookieJar','ftplib','gopherlib','_ssl',
    'sgmlib','HTMLParser','cgi','cmd','locale',
    'htmllib','httplib','mimetools','mimetypes',
    'rfc822','tty','webbrowser','socket',
    'hashlib','base64','compiler','pydoc','xml']

# Binarios Exluidos
bin_excludes=[
    'jpeg.dll','libfreetype-6.dll'
    'libogg-0.dll','libpng12-0.dll',
    'libtiff.dll','libvorbis-0.dll',
    'portmidi.dll','SDL.dll',
    'SDL_image.dll','SDL_mixer.dll',
    'SDL_ttf.dll','smpeg.dll',
    'zlib1.dll']

# Data
data_includes=[
    ('Data','Data'),
    ('../lib','')
    ]

# Setup
setup(
    name = "Breakout",
    version = "0.1.0",
    description = "Breakout",
    options = {'build_exe' : {'build_exe': '../bins/cx_freeze',
                              'optimize': 2,
                              'compressed': True,
                              'include_files': data_includes,
                              'bin_excludes': bin_excludes,
                              'excludes': exclude_modules,
                              'base': "Win32GUI"
                              },
              },
    executables = [Executable(script="main.py")])