from typing import Literal

DomainPublicDetailProvider = Literal[
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

DOMAIN_PUBLIC_DETAIL_PROVIDER_VALUES: set[DomainPublicDetailProvider] = {
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


def check_domain_public_detail_provider(value: str) -> DomainPublicDetailProvider:
    if value in DOMAIN_PUBLIC_DETAIL_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_PROVIDER_VALUES!r}")
