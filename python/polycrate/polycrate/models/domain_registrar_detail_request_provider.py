from typing import Literal

DomainRegistrarDetailRequestProvider = Literal[
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

DOMAIN_REGISTRAR_DETAIL_REQUEST_PROVIDER_VALUES: set[DomainRegistrarDetailRequestProvider] = {
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


def check_domain_registrar_detail_request_provider(value: str) -> DomainRegistrarDetailRequestProvider:
    if value in DOMAIN_REGISTRAR_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_REQUEST_PROVIDER_VALUES!r}")
