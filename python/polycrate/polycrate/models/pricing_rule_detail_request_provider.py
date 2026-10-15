from typing import Literal

PricingRuleDetailRequestProvider = Literal[
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

PRICING_RULE_DETAIL_REQUEST_PROVIDER_VALUES: set[PricingRuleDetailRequestProvider] = {
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


def check_pricing_rule_detail_request_provider(value: str) -> PricingRuleDetailRequestProvider:
    if value in PRICING_RULE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_REQUEST_PROVIDER_VALUES!r}")
