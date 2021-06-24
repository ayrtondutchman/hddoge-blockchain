from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.3",  # proof of space
    "clvm==0.9.6",
    "clvm_rs==0.1.7",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the hddoge processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="hddoge-blockchain",
    author="aDutchman",
    author_email="N/A",
    description="Hddoge blockchain full node, farmer, timelord, and wallet.",
    url="https://hddoge.org/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="hddoge blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "hddoge",
        "hddoge.cmds",
        "hddoge.consensus",
        "hddoge.daemon",
        "hddoge.full_node",
        "hddoge.timelord",
        "hddoge.farmer",
        "hddoge.harvester",
        "hddoge.introducer",
        "hddoge.plotting",
        "hddoge.protocols",
        "hddoge.rpc",
        "hddoge.server",
        "hddoge.simulator",
        "hddoge.types.blockchain_format",
        "hddoge.types",
        "hddoge.util",
        "hddoge.wallet",
        "hddoge.wallet.puzzles",
        "hddoge.wallet.rl_wallet",
        "hddoge.wallet.cc_wallet",
        "hddoge.wallet.did_wallet",
        "hddoge.wallet.settings",
        "hddoge.wallet.trading",
        "hddoge.wallet.util",
        "hddoge.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "hddoge = hddoge.cmds.hddoge:main",
            "hddoge_wallet = hddoge.server.start_wallet:main",
            "hddoge_full_node = hddoge.server.start_full_node:main",
            "hddoge_harvester = hddoge.server.start_harvester:main",
            "hddoge_farmer = hddoge.server.start_farmer:main",
            "hddoge_introducer = hddoge.server.start_introducer:main",
            "hddoge_timelord = hddoge.server.start_timelord:main",
            "hddogege_timelord_launcher = hddoge.timelord.timelord_launcher:main",
            "hddoge_full_node_simulator = hddoge.simulator.start_simulator:main",
        ]
    },
    package_data={
        "hddoge": ["pyinstaller.spec"],
        "hddoge.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "hddoge.util": ["initial-*.yaml", "english.txt"],
        "hddoge.ssl": ["hddoge_ca.crt", "hddoge_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
