# -*- coding: utf-8 -*-

import typing
import pycamunda.variable
import worker
import javaobj
import base64


def parse_report(result: pycamunda.variable.Variable) -> typing.Dict[str, str]:
    try:
        print('Generate report from result')
        print(result)

        # b = base64.b64decode(result.value)
        # j = javaobj.loads(b)
        # print('deserized')
        # print(j)
        
        print('Parse result')
        print('COMPLETED')
    except ValueError:
        raise worker.ExternalTaskException(message='invalid input')

    return {'parsed_result': 'Parse and store report'}

if __name__ == "__main__":
    parse_report('result')