import pytest

from common.extract_util import extract_util, save_variable
from common.request_util import request_utl
from common.text_util import *
from common.yaml_util import *
import json


@pytest.mark.run(order=1)
@pytest.mark.all
@pytest.mark.parametrize('args', extract_util('%s/data/case_yaml/1.登录.yaml' % base_dir))
def test_login(args):
    """登录接口，获取token"""
    url = args['url']
    headers = eval(args['header'])
    payloads = json.dumps(eval(args['body']))
    params = eval(args['body'])
    method = args["method"]
    run_result_txt = '%s/data/run_result.txt' % base_dir  # 运行结果保存到txt文件中
    expect = args['expect']  # 断言依据

    rep = request_utl(method, url, headers, payloads=payloads, params=params, expect=expect, run_result_txt=run_result_txt)

    print(rep)
    if args['id'] == 1:
        token = json.loads(rep)['data']['token']
        save_variable(key="token", value=token)




