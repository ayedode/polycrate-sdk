from typing import Literal

PatchedRegistrarTLDPriceDetailRequestProvider = Literal[
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

PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedRegistrarTLDPriceDetailRequestProvider] = {
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


def check_patched_registrar_tld_price_detail_request_provider(
    value: str,
) -> PatchedRegistrarTLDPriceDetailRequestProvider:
    if value in PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_REGISTRAR_TLD_PRICE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
