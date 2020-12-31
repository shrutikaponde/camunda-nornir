# -*- coding: utf-8 -*-

import typing
import pycamunda.variable
import worker


def run_napalm_validate(config_path: pycamunda.variable.Variable) -> typing.Dict[str, str]:
    try:
        print('Config file path')
        print(config_path)

        print('run network validation')
        print('COMPLETED')
    except ValueError:
        raise worker.ExternalTaskException(message='invalid input')

    return {'result': { 
            'status': 'SUCCESS',
            'output': {
                'nested' : 'This will contain validation result.'
                }
            }}