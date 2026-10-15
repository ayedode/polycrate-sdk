from typing import Literal

PricingQuoteDetailRequestProvider = Literal[
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

PRICING_QUOTE_DETAIL_REQUEST_PROVIDER_VALUES: set[PricingQuoteDetailRequestProvider] = {
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


def check_pricing_quote_detail_request_provider(value: str) -> PricingQuoteDetailRequestProvider:
    if value in PRICING_QUOTE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_DETAIL_REQUEST_PROVIDER_VALUES!r}")
