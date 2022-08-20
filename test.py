# -*- coding: utf-8 -*-
import re
from base64 import b64encode


def bytes_tr(json_str):
    # 如果JSON中value中有"bytes:xxx"的模式，则将bytes:xxx替换成base64编码的字符串。用于辅助输入bytes类型的字段
    return re.sub(r':\s*\"bytes\s*//(.*)(?<!\")"',
                 lambda x: ": \"%s\"" % b64encode(x.group(1).encode("utf-8")).decode("utf-8"), json_str)


if __name__ == "__main__":
    with open("json.txt", "r") as fp:
        print(bytes_tr(fp.read()))

