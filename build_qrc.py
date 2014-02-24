# gPodder Windows Build Script
# 2014-02-22 Thomas Perl <thp.io/about>
# All rights reserved.

import os

IGNORED_FILES = ['common']

# Can be touch or desktop at the moment
variant = 'touch'

def mount_files(out, source, target):
    for path, dirnames, filenames in os.walk(source):
        path = path.replace('\\', '/')
        for filename in sorted(filenames):
            if filename in IGNORED_FILES:
                continue

            from_filename = '/'.join((path, filename))
            to_filename = from_filename.replace(source, target)
            print('<file alias="%s">%s</file>' % (to_filename, from_filename), file=out)
            print(from_filename, '->', to_filename)

with open('gpodder.qrc', 'w') as out:
    print('<RCC>', file=out)
    print('<qresource prefix="/">', file=out)

    # QML UI
    mount_files(out, 'gpodder-ui-qml/%s' % variant, variant)
    mount_files(out, 'gpodder-ui-qml/common', '%s/common' % variant)

    print('</qresource>', file=out)
    print('</RCC>', file=out)
