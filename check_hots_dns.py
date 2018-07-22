#!/usr/bin/env python

import socket
from socket import gethostbyname
import dns.resolver

nameservers = [
    '1.1.1.1',
    '1.0.0.1',
    '8.8.8.8',
    '8.8.4.4'
]

client = dns.resolver.Resolver()

if __name__ == '__main__':
    domains_to_check = [
        'us-hero.logon.battle.net',
        'eu-hero.logon.battle.net',
        'kr-hero.logon.battle.net',
        'tw-hero.logon.battle.net',
    ]

    domain_is_resolveable = {}
    for nameserver in nameservers:
        client.nameservers = [
            nameserver
        ]

        print "\033[36m[ {nameserver} ]\033[0m".format(
            nameserver=nameserver
        )

        for domain in domains_to_check:
            try:
                response = client.query(domain, 'A')
                print "{domain} \033[32mOK\033[0m".format(
                    domain=domain
                )
            except dns.resolver.NXDOMAIN:
                print "{domain} \033[31mFAILED\033[0m".format(
                    domain=domain
                )

        print ''
