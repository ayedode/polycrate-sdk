from typing import Literal

PatchedDomainContactDetailRequestProvider = Literal[
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

PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedDomainContactDetailRequestProvider] = {
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


def check_patched_domain_contact_detail_request_provider(value: str) -> PatchedDomainContactDetailRequestProvider:
    if value in PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
