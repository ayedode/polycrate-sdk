from typing import Literal

OrganizationProductDetailRequestProvider = Literal[
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

ORGANIZATION_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES: set[OrganizationProductDetailRequestProvider] = {
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


def check_organization_product_detail_request_provider(value: str) -> OrganizationProductDetailRequestProvider:
    if value in ORGANIZATION_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
