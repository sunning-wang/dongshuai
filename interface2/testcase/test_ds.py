import pytest
import json

from common.extract_util import extract_util
from common.request_util import request_utl
from common.yaml_util import *

@pytest.mark.skip
@pytest.mark.parametrize('args', extract_util('%s/data/case_yaml/1.登录.yaml' % base_dir))
# @pytest.mark.skip
def test_ds01(args):

    url = args['url']
    headers = eval(args['header'])
    payloads = json.dumps(eval(args['body']))
    params = eval(args['body'])
    method = args["method"]
    run_result_txt = '%s/data/run_result.txt' % base_dir  # 运行结果保存到txt文件中
    expect = args['expect']  # 断言依据

    rep = request_utl(method, url, headers, payloads=payloads, params=params, expect=expect, run_result_txt=run_result_txt)
    print(rep)



