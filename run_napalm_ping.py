# -*- coding: utf-8 -*-

import typing
import pycamunda.variable
import worker


def run_napalm_ping(config_path: pycamunda.variable.Variable) -> typing.Dict[str, dict]:
    try:

        print('Config file path')
        print(config_path)

        print('check network conectivity')
        print('COMPLETED')
    except ValueError:
        raise worker.ExternalTaskException(message='invalid input')

    return {'result': { 
            'status': 'SUCCESS',
            'output': {
                'nested' : 'This object will contain device connectivity output'
                }
            }}