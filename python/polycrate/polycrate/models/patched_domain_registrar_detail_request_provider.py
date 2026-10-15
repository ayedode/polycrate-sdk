from typing import Literal

PatchedDomainRegistrarDetailRequestProvider = Literal[
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

PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedDomainRegistrarDetailRequestProvider] = {
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


def check_patched_domain_registrar_detail_request_provider(value: str) -> PatchedDomainRegistrarDetailRequestProvider:
    if value in PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
