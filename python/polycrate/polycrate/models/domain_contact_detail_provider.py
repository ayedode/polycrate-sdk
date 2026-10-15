from typing import Literal

DomainContactDetailProvider = Literal[
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

DOMAIN_CONTACT_DETAIL_PROVIDER_VALUES: set[DomainContactDetailProvider] = {
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


def check_domain_contact_detail_provider(value: str) -> DomainContactDetailProvider:
    if value in DOMAIN_CONTACT_DETAIL_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_PROVIDER_VALUES!r}")
