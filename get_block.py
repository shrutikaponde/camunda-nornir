# -*- coding: utf-8 -*-

import typing
import pycamunda.variable
import worker
import re
import javaobj.v2 as javaobj
import base64

def get_block(start_expression: pycamunda.variable.Variable, 
              end_expression: pycamunda.variable.Variable,
              result: pycamunda.variable.Variable
              ) -> typing.Dict[str, str]:
    try:
        print('End block expression')
        print(start_expression, end_expression)
        print('deserialize command output')
        b = base64.b64decode(result.value)
        deserialized_cmds_output = javaobj.loads(b)
        print('COMPLETED')
    except ValueError:
        raise worker.ExternalTaskException(message='invalid input')

    regex = r'' +  start_expression.value + end_expression.value
    print(regex)
    matched_grp = re.search(regex ,deserialized_cmds_output.get('output').__str__()).group()
    print('matched block', matched_grp)
    return {"matched_block": matched_grp}