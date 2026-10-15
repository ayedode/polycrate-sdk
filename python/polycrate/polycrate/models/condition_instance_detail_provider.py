from typing import Literal

ConditionInstanceDetailProvider = Literal[
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
]

CONDITION_INSTANCE_DETAIL_PROVIDER_VALUES: set[ConditionInstanceDetailProvider] = {
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
}


def check_condition_instance_detail_provider(value: str) -> ConditionInstanceDetailProvider:
    if value in CONDITION_INSTANCE_DETAIL_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_PROVIDER_VALUES!r}")
