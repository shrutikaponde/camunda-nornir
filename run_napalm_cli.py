# -*- coding: utf-8 -*-

from nornir import InitNornir
from nornir.core.inventory import Host
from nornir_napalm.plugins.tasks import napalm_cli
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
import re

# COMMANDS with filter expressions
# show ip int br | i _192\.168\.122\.50_
# show ip int br | i ^F.*up.*up ( shows all up up interfaces )

# Gives you the every line in your running config that starts with (that’s what the ^ is all about) “interface” or ” ip address”,
# show run | i ^interface|^_ip address

# Shows you all of the IP-capable interfaces on the box, except for the ones that have not been assigned an IP address.
# show ip interf brief | e unassigned


def run_napalm_cli(config_path: pycamunda.variable.Variable, commands: pycamunda.variable.Variable) -> typing.Dict[str, str]:
    try:
        print('Config file path')
        nr = InitNornir(config_file=config_path.value)


        b = base64.b64decode(commands.value)
        deserialized_cmds = javaobj.loads(b)
        cmds = [ i.__str__() for i in deserialized_cmds]
        print('run commands', cmds)

        result = nr.run(napalm_cli, commands=cmds ) #["show version", "show ip int br", "show ip route"])

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


def hello():
    nr = InitNornir(config_file="config.yaml")
    print('run commands')
    result = nr.run(napalm_cli, commands=[ "show ip int br"])
    dict_result = [result[k][0].__dict__ for k, v in result.items()]
    new_dict = {}
    for k,v in dict_result[0]['result'].items():
        new_dict[k.replace(' ', '_')] = v
    
    dict_result[0]['result'] = new_dict
    print(dict_result)
    input()
    payload = json.dumps({
        "variables":{
            "commands_output" : {
                "value": json.dumps(dict_result[0]['result'], default=encode_complex),
			    "type": "json"
		    }
	    }
    })
    
    headers = {
        'content-type': "application/json"
    }
    url = 'http://localhost:8080/engine-rest/decision-definition/key/decide_crypt_auth_enabled/evaluate'
    x = requests.post(url, data = payload, headers=headers)

    print(x.text)

def exe_dmn():

    file_path = os.path.join(os.path.dirname(__file__), 'outputs', 'cli_commands.txt')
    cmd_output = {}

    # Replace spaces with underscores for key names
    for k,v in json.load(open(file_path, 'r')).items():
        cmd_output[k.replace(' ', '_')] = v

    # Match block expression for command show ip ospf interface
    regex = r"(Vlan.*?|Tunnel.*?|FastEthernet.*?|Serial.*?|Gi.*?|Port-.*?|Ten.*?) is up,.*?(Cryptographic|Suppress)"
    matches = re.finditer(regex, cmd_output['show_ip_ospf_interface'], re.S)

    matched_blocks = []
    for matchNum, match in enumerate(matches, start=1):
        matched_blocks.append({ "block": match.group(), "groups" : list(match.groups()) })
   
    # print(matched_blocks)
    conditions = {
        "condition_1" : {},
        "condition_2" : {
            "block_expressions" : matched_blocks
        }
    }
    payload = json.dumps({
        "variables":{
            "commands_output" : {
                "value": json.dumps(cmd_output),
			    "type": "json"
		    },
            "conditions" : {
                "value": json.dumps(conditions),
			    "type": "json"
		    }
	    }
    })
    # exit()
    
    headers = {
        'content-type': "application/json"
    }
    url = 'http://localhost:8080/engine-rest/decision-definition/key/decide_crypt_auth_enabled/evaluate'
    response = requests.post(url, data = payload, headers=headers)
    print(response.json())


if __name__ == "__main__":
    exe_dmn()