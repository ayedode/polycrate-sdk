from typing import Literal

CatalogueAppDetailRequestProvider = Literal[
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

CATALOGUE_APP_DETAIL_REQUEST_PROVIDER_VALUES: set[CatalogueAppDetailRequestProvider] = {
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


def check_catalogue_app_detail_request_provider(value: str) -> CatalogueAppDetailRequestProvider:
    if value in CATALOGUE_APP_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_REQUEST_PROVIDER_VALUES!r}")
