expected_output = {
    "bridge_group":{
        "NETWORK":{
            "bridge_domain":{
                "NETWORK_680_1":{
                    "id":0,
                    "state":"up",
                    "shg_id":0,
                    "mst_i":0,
                    "mac_aging_time":300,
                    "mac_limit":16000,
                    "mac_limit_action":"none",
                    "mac_limit_notification":"syslog, trap",
                    "filter_mac_address":0,
                    "ac":{
                        "num_ac":1,
                        "num_ac_up":1,
                        "interfaces":{
                            "HundredGigE0/1/0/1.1":{
                                "state":"up",
                                "static_mac_address":0
                            }
                        }
                    },
                    "vfi":{
                        "num_vfi":1,
                        "IBR_NETWORK_680_1":{
                            "state":"up",
                            "neighbor":{
                                "192.168.201.1":{
                                    "pw_id":{
                                        1513:{
                                            "state":"up",
                                            "static_mac_address":0
                                        },
                                        1514:{
                                            "state":"up",
                                            "static_mac_address":0
                                        },
                                        1680:{
                                            "state":"up",
                                            "static_mac_address":0
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "pw":{
                        "num_pw":5,
                        "num_pw_up":5,
                        "neighbor":{
                            "192.168.201.1":{
                                "pw_id":{
                                    1630:{
                                        "state":"up",
                                        "static_mac_address":0
                                    }
                                }
                            },
                            "192.168.201.2":{
                                "pw_id":{
                                    1630:{
                                        "state":"up",
                                        "static_mac_address":0
                                    }
                                }
                            }
                        }
                    },
                    "pbb":{
                        "num_pbb":0,
                        "num_pbb_up":0
                    },
                    "vni":{
                        "num_vni":0,
                        "num_vni_up":0
                    }
                }
            }
        }
    }
}
