
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.ios.show_vrf import ShowVrfDetail, ShowVrf

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

 
# ================================
#  Unit test for 'show vrf detail'
# ================================

class test_show_vrf_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'VRF1': {'address_family': {'ipv4 unicast': {'flags': '0x0',
                                                      'route_targets': {'100:1': {'route_target': '100:1',
                                                                                  'rt_type': 'both'}},
                                                      'table_id': '0x1',
                                                      'vrf_label': {'allocation_mode': 'per-prefix'}},
                                     'ipv6 unicast': {'flags': '0x0',
                                                      'route_targets': {'100:1': {'route_target': '100:1',
                                                                                  'rt_type': 'both'}},
                                                      'table_id': '0x1E000001',
                                                      'vrf_label': {'allocation_mode': 'per-prefix'}}},
                  'flags': '0x180C',
                  'interfaces': ['Loopback1', 'GigabitEthernet0/4.200'],
                  'interface': {'Loopback1': {'vrf': 'VRF1'},
                                'GigabitEthernet0/4.200': {'vrf': 'VRF1'}},
                  'route_distinguisher': '100:1',
                  'vrf_id': 1},
         'VRF2': {'address_family': {'ipv4 unicast': {'flags': '0x0',
                                                      'table_id': '0x2',
                                                      'vrf_label': {'allocation_mode': 'per-prefix'}},
                                     'ipv6 unicast': {'flags': '0x0',
                                                      'table_id': '0x1E000002',
                                                      'vrf_label': {'allocation_mode': 'per-prefix'}}},
                  'flags': '0x1808',
                  'vrf_id': 2}
    }


    golden_output = {'execute.return_value': '''
        VRF VRF1 (VRF Id = 1); default RD 100:1; default VPNID <not set>
          New CLI format, supports multiple address-families
          Flags: 0x180C
          Interfaces:
            Lo1                      Gi0/4.200               
        Address family ipv4 unicast (Table ID = 0x1):
          Flags: 0x0
          Export VPN route-target communities
            RT:100:1                
          Import VPN route-target communities
            RT:100:1                
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv6 unicast (Table ID = 0x1E000001):
          Flags: 0x0
          Export VPN route-target communities
            RT:100:1                
          Import VPN route-target communities
            RT:100:1                
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv4 multicast not active

        VRF VRF2 (VRF Id = 2); default RD <not set>; default VPNID <not set>
          New CLI format, supports multiple address-families
          Flags: 0x1808
          No interfaces
        Address family ipv4 unicast (Table ID = 0x2):
          Flags: 0x0
          No Export VPN route-target communities
          No Import VPN route-target communities
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv6 unicast (Table ID = 0x1E000002):
          Flags: 0x0
          No Export VPN route-target communities
          No Import VPN route-target communities
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        Address family ipv4 multicast not active
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVrfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

class test_show_vrf(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        [2019-05-10 06:56:37,856] +++ R1_xe: executing command 'show vrf' +++
        show vrf
        Name                             Default RD            Protocols   Interfaces
        Mgmt-intf                        <not set>             ipv4,ipv6   Gi1
        VRF1                             65000:1               ipv4,ipv6   Tu1
                                                                            Lo300
                                                                            Gi2.390
                                                                            Gi2.410
                                                                            Gi2.415
                                                                            Gi2.420
                                                                            Gi3.390
                                                                            Gi3.410
                                                                            Gi3.415
                                                                            Tu3
                                                                            Tu4
                                                                            Tu6
                                                                            Tu8
                                                                            Gi3.420
    '''}

    golden_parsed_output = {
        'vrf': {
            'Mgmt-intf': {
                'protocols': ['ipv4', 'ipv6'],
                'interfaces': ['GigabitEthernet1'],
            },
            'VRF1': {
                'route_distinguisher': '65000:1',
                'protocols': ['ipv4', 'ipv6'],
                'interfaces': ['Tunnel1',
                               'Loopback300',
                               'GigabitEthernet2.390',
                               'GigabitEthernet2.410',
                               'GigabitEthernet2.415',
                               'GigabitEthernet2.420',
                               'GigabitEthernet3.390',
                               'GigabitEthernet3.410',
                               'GigabitEthernet3.415',
                               'Tunnel3',
                               'Tunnel4',
                               'Tunnel6',
                               'Tunnel8',
                               'GigabitEthernet3.420'],
            }
        }
    }

    golden_output_vrf = {'execute.return_value': '''
        [2019-05-10 06:56:43,272] +++ R1_xe: executing command 'show vrf VRF1' +++
        show vrf VRF1
        Name                             Default RD            Protocols   Interfaces
        VRF1                             65000:1               ipv4,ipv6   Tu1
                                                                            Lo300
                                                                            Gi2.390
                                                                            Gi2.410
                                                                            Gi2.415
                                                                            Gi2.420
                                                                            Gi3.390
                                                                            Gi3.410
                                                                            Gi3.415
                                                                            Tu3
                                                                            Tu4
                                                                            Tu6
                                                                            Tu8
                                                                            Gi3.420
    '''}

    golden_parsed_output_vrf = {
        'vrf': {
            'VRF1': {
                'route_distinguisher': '65000:1',
                'protocols': ['ipv4', 'ipv6'],
                'interfaces': ['Tunnel1',
                               'Loopback300',
                               'GigabitEthernet2.390',
                               'GigabitEthernet2.410',
                               'GigabitEthernet2.415',
                               'GigabitEthernet2.420',
                               'GigabitEthernet3.390',
                               'GigabitEthernet3.410',
                               'GigabitEthernet3.415',
                               'Tunnel3',
                               'Tunnel4',
                               'Tunnel6',
                               'Tunnel8',
                               'GigabitEthernet3.420'],
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVrf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf(self):
        self.device = Mock(**self.golden_output_vrf)
        obj = ShowVrf(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf)

if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
