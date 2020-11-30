# pylint: disable-all
from io import StringIO, BytesIO, FileIO  # pylint: disable=unused-import
import sys

cmd = ['pylint', 'autohooks/plugins/pylint/pylint.py']
import subprocess  # pylint: disable=

# status = subprocess.call(cmd)
iofile = 'tmp.txt'
# status = subprocess.call(cmd, stdout=iofile)
# blah blah lots of code ...

status = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = status.communicate()
print(out.decode(encoding='utf-8'))
print(err.decode(encoding='utf-8'))
