from setuptools import setup


setup(
    name="pyagentx-async",
    version="0.1.0",
    author="Ernst de Vries",
    author_email="ernst.de.vries@gmail.com",
    description=("AgentX package to extend SNMP with pure Python3.10"),
    license="BSD",
    keywords="snmp network agentx ",
    url="https://github.com/ejvr/pyagentx3",
    packages=['pyagentx3'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Environment :: No Input/Output (Daemon)",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
    ],
    long_description='''\
PyAgentXAsync
--------------------
PyAgentXAsync is a pure Python3 implementation of AgentX protocol (RFC 2741),
using non-block (async) communication. It is a rewrite of Richard Prinz's PyAgentX3.

The agent can support the following commands:
- snmpget
- snmpwalk
- snmptable
- snmpset

It also allows sending notifications/traps.
''',
)
