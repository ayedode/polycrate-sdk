from typing import Literal

RegistrarTLDPriceDetailRequestProvider = Literal[
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

REGISTRAR_TLD_PRICE_DETAIL_REQUEST_PROVIDER_VALUES: set[RegistrarTLDPriceDetailRequestProvider] = {
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


def check_registrar_tld_price_detail_request_provider(value: str) -> RegistrarTLDPriceDetailRequestProvider:
    if value in REGISTRAR_TLD_PRICE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
