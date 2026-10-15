from typing import Literal

RegistrarTLDPriceDetailProvider = Literal[
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

REGISTRAR_TLD_PRICE_DETAIL_PROVIDER_VALUES: set[RegistrarTLDPriceDetailProvider] = {
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


def check_registrar_tld_price_detail_provider(value: str) -> RegistrarTLDPriceDetailProvider:
    if value in REGISTRAR_TLD_PRICE_DETAIL_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_PROVIDER_VALUES!r}")
