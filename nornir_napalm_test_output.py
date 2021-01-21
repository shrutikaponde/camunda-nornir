# -*- coding: utf-8 -*-

from nornir import InitNornir
from nornir.core.inventory import Host
from nornir_napalm.plugins.tasks import napalm_cli, napalm_get
from nornir_utils.plugins.functions import print_result

import os
import pprint
import requests
import typing
import pycamunda.variable
import worker
import json
import javaobj
import base64

def encode_complex(z):
    if isinstance(z, Host):
        return z.dict()
    else:
        return z

def get_commands(cmds, f):
    nr = InitNornir(config_file="config.yaml")

    print('get information')
    result = nr.run(task=napalm_get,getters=cmds, destination='192.168.122.1')

    f.write(json.dumps(result['r1'][0].result, default=encode_complex))
    f.close()

def cli_commands(cmds, f):
    nr = InitNornir(config_file="config.yaml")

    print('run commands')
    result = nr.run(napalm_cli, commands=cmds)
    print_result(result)
    dict_result = [result[k][0].__dict__ for k, v in result.items()]
    f.write("++++++++++++++++++ RAW STRING OUTPUT (napalm cli ) ++++++++++++++++++\n\n")
    f.write(json.dumps(dict_result[0]['result'], default=encode_complex))
    f.close()

if __name__ == "__main__":

    print(os.path.join(os.path.dirname(__file__),'config.ini'))
    exit()
    cmds = ["show ip int br","show snmp user", "show run", "show running-config", "show ip ospf interface", "show ip route"]
    g_cmds= ["facts", "config", "interfaces", "bgp_neighbors"]
    
    # f = open("interfaces.txt", "w")
    # cli_commands(["show ip int br"], f)
    # f = open("interfaces.txt", "a")
    # f.write("\n\n++++++++++++++++++ STRUCTURED OUTPUT (napalm get ) ++++++++++++++++++\n\n")    
    # get_commands(["interfaces"], f)

    # f = open("config.txt", "w")
    # cli_commands(["show run"], f)
    # f = open("config.txt", "a")
    # f.write("\n\n++++++++++++++++++ STRUCTURED OUTPUT (napalm get ) ++++++++++++++++++\n\n")    
    # get_commands(["config"], f)

    f = open("show_ip_route.txt", "w")
    cli_commands(["show ip route"], f)
    f = open("show_ip_route.txt", "a")
    f.write("\n\n++++++++++++++++++ STRUCTURED OUTPUT (napalm get ) ++++++++++++++++++\n\n")    
    get_commands(["route_to"], f)


    # f = open("snmp_information.txt", "w")
    # cli_commands(["show snmp user"], f)
    # f = open("snmp_information.txt", "a")
    # f.write("\n\n++++++++++++++++++ STRUCTURED OUTPUT (napalm get ) ++++++++++++++++++\n\n")    
    # # get_commands(["snmp_user"], f)