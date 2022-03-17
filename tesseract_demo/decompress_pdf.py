import re
import zlib
import traceback


PDF_file = "/Users/chibinjiang/Downloads/0106002.pdf"
# zhutao@cqu.edu.cn
pdf = open(PDF_file, "rb").read()
stream = re.compile(b'.*?FlateDecode.*?stream(.*?)endstream', re.S)

content = b''

for s in re.findall(stream, pdf)[-2:]:
    s = s.strip(b'\r\n')
    try:
        content += zlib.decompress(s)  # .decode('utf8', errors='ignore')
    except Exception:
        traceback.print_exc()

import ipdb; ipdb.set_trace()
