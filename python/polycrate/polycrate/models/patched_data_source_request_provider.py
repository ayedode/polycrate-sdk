from typing import Literal

PatchedDataSourceRequestProvider = Literal[
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

PATCHED_DATA_SOURCE_REQUEST_PROVIDER_VALUES: set[PatchedDataSourceRequestProvider] = {
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


def check_patched_data_source_request_provider(value: str) -> PatchedDataSourceRequestProvider:
    if value in PATCHED_DATA_SOURCE_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DATA_SOURCE_REQUEST_PROVIDER_VALUES!r}")
