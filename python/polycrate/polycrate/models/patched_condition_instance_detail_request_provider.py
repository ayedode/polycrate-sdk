from typing import Literal

PatchedConditionInstanceDetailRequestProvider = Literal[
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

PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedConditionInstanceDetailRequestProvider] = {
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


def check_patched_condition_instance_detail_request_provider(
    value: str,
) -> PatchedConditionInstanceDetailRequestProvider:
    if value in PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
