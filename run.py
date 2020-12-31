# -*- coding: utf-8 -*-

import random
import typing
import pycamunda.variable
import worker
from parse_report import parse_report
from run_napalm_validate import run_napalm_validate
from run_napalm_ping import run_napalm_ping
from run_napalm_cli import run_napalm_cli

if __name__ == '__main__':
    import pycamunda.processdef

    url = 'http://localhost:8080/engine-rest'
    worker_id = '1'

    # start_instance = pycamunda.processdef.StartInstance(url=url, key='Audit_001')
    # start_instance.add_variable(name='config_path', value='config.yaml')

    # for _ in range(3):
    #     start_instance()

    # exit()
    worker = worker.Worker(url=url, worker_id=worker_id)
    # worker.subscribe(
    #     topic='check_inventory',
    #     func=check_inventory,
    #     variables=['config_path']
    # )
    # print('Subscribed to check_inventory topic')

    worker.subscribe(
        topic='napalm_get',
        func=run_napalm_cli,
        variables=['config_path', 'commands']
    )
    print('Subscribed to napalm_cli topic')


    worker.subscribe(
        topic='napalm_ping',
        func=run_napalm_ping,
        variables=['config_path']
    )
    print('Subscribed to napalm_ping topic')

    worker.subscribe(
        topic='parse_report',
        func=parse_report,
        variables=['result']
    )
    print('Subscribed to parsed_report topic')

    worker.subscribe(
        topic='napalm_validate',
        func=run_napalm_validate,
        variables=['config_path']
    )
    print('Subscribed to napalm_validate topic')


    worker.run()
