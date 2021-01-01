# -*- coding: utf-8 -*-

import typing
import pycamunda.variable
import worker


def run_napalm_cli(config_path: pycamunda.variable.Variable, commands: pycamunda.variable.Variable) -> typing.Dict[str, str]:
    try:
        print('Config file path')
        print(config_path)

        print('run commands')
        print('COMPLETED')
    except ValueError:
        raise worker.ExternalTaskException(message='invalid input')

    return {'result': { 
            'status': 'SUCCESS',
            'interface':  '192.168.1.1'
            }}