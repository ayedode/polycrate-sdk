from typing import Literal

ConditionInstanceDetailRequestProvider = Literal[
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

CONDITION_INSTANCE_DETAIL_REQUEST_PROVIDER_VALUES: set[ConditionInstanceDetailRequestProvider] = {
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


def check_condition_instance_detail_request_provider(value: str) -> ConditionInstanceDetailRequestProvider:
    if value in CONDITION_INSTANCE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
