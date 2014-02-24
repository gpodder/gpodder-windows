# gPodder Windows Build Script
# 2014-02-22 Thomas Perl <thp.io/about>
# All rights reserved.

import os
import zipfile

IGNORED_FILES = ['common']

def mount_file(out, source, target):
    print('%s -> %s' % (source, target))
    out.write(source, target)

def mount_files(out, source, target, ext):
    for path, dirnames, filenames in os.walk(source):
        path = path.replace('\\', '/')
        for filename in sorted(filenames):
            if filename in IGNORED_FILES or not filename.endswith(ext):
                continue

            from_filename = '/'.join((path, filename))
            to_filename = from_filename.replace(source, target)
            print('%s -> %s' % (from_filename, to_filename))
            out.write(from_filename, to_filename)

out = zipfile.ZipFile('gpodder.zip', 'w')

# QML UI
mount_file(out, 'gpodder-ui-qml/main.py', 'main.py')

# gPodder Core
mount_files(out, 'gpodder-core/src/gpodder', 'gpodder', '.py')
mount_file(out, 'gpodder-core/src/jsonconfig.py', 'jsonconfig.py')

# Podcastparser
mount_file(out, 'podcastparser/podcastparser.py', 'podcastparser.py')

out.close()
