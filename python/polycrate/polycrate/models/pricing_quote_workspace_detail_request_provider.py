from typing import Literal

PricingQuoteWorkspaceDetailRequestProvider = Literal[
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

PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_PROVIDER_VALUES: set[PricingQuoteWorkspaceDetailRequestProvider] = {
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


def check_pricing_quote_workspace_detail_request_provider(value: str) -> PricingQuoteWorkspaceDetailRequestProvider:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
