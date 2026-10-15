from typing import Literal

PatchedCatalogueAppDetailRequestProvider = Literal[
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

PATCHED_CATALOGUE_APP_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedCatalogueAppDetailRequestProvider] = {
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


def check_patched_catalogue_app_detail_request_provider(value: str) -> PatchedCatalogueAppDetailRequestProvider:
    if value in PATCHED_CATALOGUE_APP_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CATALOGUE_APP_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
