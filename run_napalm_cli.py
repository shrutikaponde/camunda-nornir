# -*- coding: utf-8 -*-

from nornir import InitNornir
from nornir.core.inventory import Host
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result

import pprint

import typing
import pycamunda.variable
import worker
import json

def run_napalm_cli(config_path: pycamunda.variable.Variable, commands: pycamunda.variable.Variable) -> typing.Dict[str, str]:
    try:
        print('Config file path')
        nr = InitNornir(config_file=config_path.value)

        print('run commands')
        result = nr.run(napalm_cli, commands=["show version", "show ip int br", "show ip route"])

        print('COMPLETED')
    except ValueError:
        raise worker.ExternalTaskException(message='invalid input')

    dict_result = [result[k][0].__dict__ for k, v in result.items()]
    json_result = json.dumps(dict_result, default=encode_complex)
    print(json_result)
    return {'result': { 
            'status': 'SUCCESS',
            'output' : json_result
            }}

def encode_complex(z):
    if isinstance(z, Host):
        return z.dict()
    else:
        return z
