# -*- coding: utf-8 -*-

import random
import typing
import pycamunda.variable
import worker


def check_inventory(config_path: pycamunda.variable.Variable) -> typing.Dict[str, str]:
    try:
        print('audit details configured successfully ...')
        print('check inventory complete')
    except ValueError:
        raise worker.ExternalTaskException(message='invalid input')

    return {'number': 'number'}


def run_connectivity_test(number: pycamunda.variable.Variable) -> typing.Dict:
    print('Run connectivity test for configured IOS devices....\n\n')
    print('COMPLETED...')
    return {}


if __name__ == '__main__':
    import pycamunda.processdef

    url = 'http://localhost:8080/engine-rest'
    worker_id = '1'

    start_instance = pycamunda.processdef.StartInstance(url=url, key='Audit_001')
    start_instance.add_variable(name='config_path', value='config.yaml')

    # for _ in range(3):
    #     start_instance()

    # exit()
    worker = worker.Worker(url=url, worker_id=worker_id)
    worker.subscribe(
        topic='check_inventory',
        func=check_inventory,
        variables=['config_path']
    )
    print('Subscribed to check_inventory topic')

    worker.subscribe(
        topic='run_connectivity_test_ios',
        func=run_connectivity_test,
        variables=['number']
    )
    print('Subscribed to run_connectivity_test_ios topic')


    worker.run()
