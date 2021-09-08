import pytest
from common.extract_util import extract_util
from common.request_util import request_utl
from common.yaml_util import *
import json


@pytest.mark.smoke
@pytest.mark.parametrize('args', extract_util(case_file='%s/data/case_yaml/smoke.yaml' % base_dir))
def test_user_experience(args):
    """冒烟用例"""
    url = args['url']
    headers = eval(args['header'])
    payloads = json.dumps(eval(args['body']))
    params = eval(args['body'])
    method = args["method"]
    run_result_txt = '%s/data/run_result.txt' % base_dir  # 运行结果保存到txt文件中
    expect = args['expect']  # 断言依据

    rep = request_utl(method, url, headers, payloads=payloads, params=params, expect=expect, run_result_txt=run_result_txt)
    print("rep is :", rep)
