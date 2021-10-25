expected_output = {
    "feature":{
        "appqoe":{
            "global":{
                "ip_non_tcp_pkts":39908,
                "not_enabled":0,
                "cft_handle_pkt":0,
                "sdvt_divert_req_fail":10652,
                "appqoe_sn_data_pkts_processed":0,
                "appqoe_alloc_empty_ht_entry":6,
                "appqoe_cvla_alloc_failure":0,
                "appqoe_bulk_upd_mem_bm_no_sng":0,
                "appqoe_srv_chain_transit_dre_bypass":0,
                "appqoe_srv_chain_sn_unhealthy_bypass":0,
                "appqoe_srv_chain_tcp_mid_flow_bypass":0,
                "appqoe_srv_chain_non_tcp_bypass":0,
                "appqoe_srv_chain_frag_bypass":0,
                "appqoe_lb_without_dre":70,
                "appqoe_svc_on_appqoe_vpn_drop":0,
                "sdvt_global_stats":{
                    "within_sdvt_syn_policer_limit":18230316
                }
            },
            "sng":{
                "1":{
                    "sn_index":{
                        "0 (Green)":{
                            "ip":"26.126.0.1",
                            "oce_id":1243615088,
                            "appnav_stats":{
                                "to_sn":{
                                    "packets":444389344,
                                    "bytes":165692601033
                                },
                                "from_sn":{
                                    "packets":601788819,
                                    "bytes":485448861120
                                }
                            },
                            "sdvt_count_stats":{
                                "active_connections":19240,
                                "decaps":595905612,
                                "encaps":444389344,
                                "expired_connections":5883138,
                                "decap_messages":{
                                    "processed_control_messages":5883207,
                                    "delete_requests_recieved":5883207,
                                    "deleted_protocol_decision":5883207
                                }
                            },
                            "sdvt_packet_stats":{
                                "divert":{
                                    "packets":444389345,
                                    "bytes":144361912573
                                },
                                "reinject":{
                                    "packets":592398063,
                                    "bytes":444493781172
                                }
                            },
                            "sdvt_drop_cause_stats":{
                                
                            },
                            "sdvt_errors_stats":{
                                
                            }
                        },
                        "1 (Green)":{
                            "ip":"26.126.0.2",
                            "oce_id":1243615120,
                            "appnav_stats":{
                                "to_sn":{
                                    "packets":446327365,
                                    "bytes":165858875148
                                },
                                "from_sn":{
                                    "packets":602083263,
                                    "bytes":484834747674
                                }
                            },
                            "sdvt_count_stats":{
                                "active_connections":19016,
                                "decaps":596210922,
                                "encaps":446327365,
                                "expired_connections":5872287,
                                "decap_messages":{
                                    "processed_control_messages":5872347,
                                    "delete_requests_recieved":5872347,
                                    "deleted_protocol_decision":5872347
                                }
                            },
                            "sdvt_packet_stats":{
                                "divert":{
                                    "packets":446327366,
                                    "bytes":144435161680
                                },
                                "reinject":{
                                    "packets":592480236,
                                    "bytes":443905897996
                                }
                            },
                            "sdvt_drop_cause_stats":{
                                
                            },
                            "sdvt_errors_stats":{
                                
                            }
                        }
                    }
                },
                "2":{
                    "sn_index":{
                        "2 (Green)":{
                            "ip":"26.126.0.3",
                            "oce_id":1243615056,
                            "appnav_stats":{
                                "to_sn":{
                                    "packets":436847620,
                                    "bytes":181773622730
                                },
                                "from_sn":{
                                    "packets":563320980,
                                    "bytes":414584184530
                                }
                            },
                            "sdvt_count_stats":{
                                "active_connections":16725,
                                "decaps":557013132,
                                "encaps":436847620,
                                "expired_connections":6307881,
                                "idle_timed_out_persistent_connections":76,
                                "decap_messages":{
                                    "processed_control_messages":6307849,
                                    "delete_requests_recieved":6307849,
                                    "deleted_protocol_decision":6307849
                                }
                            },
                            "sdvt_packet_stats":{
                                "divert":{
                                    "packets":436847620,
                                    "bytes":160804936970
                                },
                                "reinject":{
                                    "packets":553758431,
                                    "bytes":375978006442
                                }
                            },
                            "sdvt_drop_cause_stats":{
                                "packets_dropped_as_sn_unhealthy":912
                            },
                            "sdvt_errors_stats":{
                                
                            }
                        }
                    }
                }
            },
            "sn_index":{
                "Default":{
                    "sdvt_count_stats":{
                        "packets_unmarked_in_ingress":797,
                        "expired_connections":105447,
                        "non_syn_divert_requests":10652
                    },
                    "sdvt_packet_stats":{
                        
                    },
                    "sdvt_drop_cause_stats":{
                        
                    },
                    "sdvt_errors_stats":{
                        "flows_bypassed_as_sn_unhealthy":105447
                    }
                }
            }
        }
    }
}
