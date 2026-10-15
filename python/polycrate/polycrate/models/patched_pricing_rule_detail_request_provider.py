from typing import Literal

PatchedPricingRuleDetailRequestProvider = Literal[
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

PATCHED_PRICING_RULE_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedPricingRuleDetailRequestProvider] = {
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


def check_patched_pricing_rule_detail_request_provider(value: str) -> PatchedPricingRuleDetailRequestProvider:
    if value in PATCHED_PRICING_RULE_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_RULE_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
