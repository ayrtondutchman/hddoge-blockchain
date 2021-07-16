from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "hddoge_harvester hddoge_timelord_launcher hddoge_timelord hddoge_farmer hddoge_full_node hddoge_wallet".split(),
    "node": "hddoge_full_node".split(),
    "harvester": "hddoge_harvester".split(),
    "farmer": "hddoge_harvester hddoge_farmer hddoge_full_node hddoge_wallet".split(),
    "farmer-no-wallet": "hddoge_harvester hddoge_farmer hddoge_full_node".split(),
    "farmer-only": "hddoge_farmer".split(),
    "timelord": "hddoge_timelord_launcher hddoge_timelord hddoge_full_node".split(),
    "timelord-only": "hddoge_timelord".split(),
    "timelord-launcher-only": "hddoge_timelord_launcher".split(),
    "wallet": "hddoge_wallet hddoge_full_node".split(),
    "wallet-only": "hddoge_wallet".split(),
    "introducer": "hddoge_introducer".split(),
    "simulator": "hddoge_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
