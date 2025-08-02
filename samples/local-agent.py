#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import socket
import sys

import pyagentx3.network
sys.path.insert(0,'..')

# --------------------------------------------
import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
logger = logging.getLogger('pyagentx3.main')
logger.addHandler(NullHandler())
# --------------------------------------------
import pyagentx3


async def send_traps(network: pyagentx3.network.Network, root_oid):
    count: int = 0
    while True:
        network.publish(
            root_oid,
            network.value_OCTETSTRING('3.0', f'String for NET-SNMP-EXAMPLES-MIB {count}'),
            network.value_OBJECTIDENTIFIER('4.0', '1.3.6.1.4.1.8072.2.4.0'),
            network.value_INTEGER('2.0', count))
        count += 1
        network.send_trap('1.3.6.1.4.1.8072.2.0.1')
        await asyncio.sleep(1)


async def main():
    pyagentx3.setup_logging(debug=False)

    try:
        pyagentx3.SOCKET_PATH = ('127.0.0.1', 705)
        root_oid = '1.3.6.1.4.1.8072.2'
        network = pyagentx3.network.Network([root_oid], {}, "AGNT", socket.AF_INET, pyagentx3.SOCKET_PATH)
        async with asyncio.TaskGroup() as tg:
            tg.create_task(network.run())
            tg.create_task(send_traps(network, root_oid))
    except Exception as ex:
        logging.fatal("Unhandled exception: %s" % ex)
        await network.stop()
        raise ex
    except KeyboardInterrupt:
        await network.stop()

if __name__ == "__main__":
    asyncio.run(main())

