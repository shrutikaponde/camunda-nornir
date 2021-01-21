# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re


regex = r"(Vlan.*?|Tunnel.*?|FastEthernet.*?|Serial.*?|Gi.*?|Port-.*?|Ten.*?) is up,.*?(Cryptographic|Suppress)"

test_str = "FastEthernet0/0 is up, line protocol is up \n  Internet Address 192.168.122.50/24, Area 0 \n  Process ID 1, Router ID 10.1.1.254, Network Type BROADCAST, Cost: 10\n  Transmit Delay is 1 sec, State DR, Priority 1 \n  Designated Router (ID) 10.1.1.254, Interface address 192.168.122.50\n  No backup designated router on this network\n  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5\n    oob-resync timeout 40\n    Hello due in 00:00:01\n  Supports Link-local Signaling (LLS)\n  Index 2/2, flood queue length 0\n  Next 0x0(0)/0x0(0)\n  Last flood scan length is 0, maximum is 0\n  Last flood scan time is 0 msec, maximum is 0 msec\n  Neighbor Count is 0, Adjacent neighbor count is 0 \n  Suppress hello for 0 neighbor(s)\nFastEthernet0/1 is up, line protocol is up \n  Internet Address 10.1.1.254/24, Area 0 \n  Process ID 1, Router ID 10.1.1.254, Network Type BROADCAST, Cost: 10\n  Transmit Delay is 1 sec, State DR, Priority 1 \n  Designated Router (ID) 10.1.1.254, Interface address 10.1.1.254\n  No backup designated router on this network\n  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5\n    oob-resync timeout 40\n    Hello due in 00:00:01\n  Supports Link-local Signaling (LLS)\n  Index 1/1, flood queue length 0\n  Next 0x0(0)/0x0(0)\n  Last flood scan length is 0, maximum is 0\n  Last flood scan time is 0 msec, maximum is 0 msec\n  Neighbor Count is 0, Adjacent neighbor count is 0 \n  Suppress hello for 0 neighbor(s)"

matches = re.finditer(regex, test_str, re.S)
# matches = re.finditer(regex, test_str, re.MULTILINE)
# print(matches)
matched_blocks = []
for matchNum, match in enumerate(matches, start=1):
    # print(match.group(), match.groups())
    matched_blocks.append({ "block": match.group(), "groups" : list(match.groups()) })
    # print ("\nMatch {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    # for groupNum in range(0, len(match.groups())):
    #     groupNum = groupNum + 1
        
    #     print ("\nGroup {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

print(matched_blocks)
# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
