from typing import Literal

PatchedDNSRecordDetailRequestProvider = Literal[
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

PATCHED_DNS_RECORD_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedDNSRecordDetailRequestProvider] = {
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


def check_patched_dns_record_detail_request_provider(value: str) -> PatchedDNSRecordDetailRequestProvider:
    if value in PATCHED_DNS_RECORD_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_RECORD_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
