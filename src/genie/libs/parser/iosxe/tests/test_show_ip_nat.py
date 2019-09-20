#!/bin/env python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_ip_nat import ShowIpNatTranslations


####################################################
# Unit test for:
#   * 'show ip nat translations'
#   * 'show ip nat translations verbose'
####################################################

class TestShowIpNatTranslations(unittest.TestCase):

    golden_output = {'execute.return_value': '''\
        Device# show ip nat translations

		Pro  Inside global         Inside local          Outside local         Outside global
		udp  10.5.5.1:1025          192.0.2.1:4000        ---                   ---
		udp  10.5.5.1:1024          192.0.2.3:4000        ---                   ---
        udp  10.5.5.1:1026          192.0.2.2:4000        ---                   ---
    '''
    }

    golden_parsed_output = {
        'nat_translations': {
            'index': {
                1: {
                    'inside_global': '10.5.5.1:1025',
                    'inside_local': '192.0.2.1:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                },
                2: {
                    'inside_global': '10.5.5.1:1024',
                    'inside_local': '192.0.2.3:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                },
                3: {
                    'inside_global': '10.5.5.1:1026',
                    'inside_local': '192.0.2.2:4000',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': 'udp'
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global      Inside local       Outside local      Outside global
        --- 171.69.233.209     192.168.1.95       ---                ---
        --- 171.69.233.210     192.168.1.89       ---                --
    '''
    }

    golden_parsed_output_1 = {
        'nat_translations': {
            'index': {
                1: {
                    'inside_global': '171.69.233.209',
                    'inside_local': '192.168.1.95',
                    'outside_global': '---',
                    'outside_local': '---',
                    'protocol': '---'
                },
                2: {
                    'inside_global': '171.69.233.210',
                    'inside_local': '192.168.1.89',
                    'outside_global': '--',
                    'outside_local': '---',
                    'protocol': '---'
                }
            }
        }
    }
    golden_output_2 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global        Inside local       Outside local      Outside global
        udp 171.69.233.209:1220  192.168.1.95:1220  171.69.2.132:53    171.69.2.132:53
        tcp 171.69.233.209:11012 192.168.1.89:11012 171.69.1.220:23    171.69.1.220:23
        tcp 171.69.233.209:1067  192.168.1.95:1067  171.69.1.161:23    171.69.1.161:23
    '''
    }

    golden_parsed_output_2 = {
        'nat_translations': {
            'index': {
                1: {
                    'inside_global': '171.69.233.209:1220',
                    'inside_local': '192.168.1.95:1220',
                    'outside_global': '171.69.2.132:53',
                    'outside_local': '171.69.2.132:53',
                    'protocol': 'udp'
                },
                2: {
                    'inside_global': '171.69.233.209:11012',
                    'inside_local': '192.168.1.89:11012',
                    'outside_global': '171.69.1.220:23',
                    'outside_local': '171.69.1.220:23',
                    'protocol': 'tcp'
                },
                3: {'inside_global': '171.69.233.209:1067',
                    'inside_local': '192.168.1.95:1067',
                    'outside_global': '171.69.1.161:23',
                    'outside_local': '171.69.1.161:23',
                    'protocol': 'tcp'
                }
            }
        }
    }

    device = Device(name='c3850')
    dev_empty = Device(name='empty')
    empty_output = {'execute.return_value': '  '}

    def test_empty(self):
        self.dev_empty = Mock(**self.empty_output)
        obj = ShowIpNatTranslations(device=self.dev_empty)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse()
        import pprint
        pprint.pprint(parsed_output)
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse()
        import pprint
        pprint.pprint(parsed_output)
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpNatTranslations(device=self.device)
        parsed_output = obj.parse()
        import pprint
        pprint.pprint(parsed_output)
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()
