from typing import Literal

PatchedPricingRuleDetailRequestProductKindType2Type1 = Literal[
    "",
    "assistant",
    "block-storage",
    "dnszone",
    "domain",
    "endpoint-monitor",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "registry-storage",
    "secrets-namespace",
    "support",
]

PATCHED_PRICING_RULE_DETAIL_REQUEST_PRODUCT_KIND_TYPE_2_TYPE_1_VALUES: set[
    PatchedPricingRuleDetailRequestProductKindType2Type1
] = {
    "",
    "assistant",
    "block-storage",
    "dnszone",
    "domain",
    "endpoint-monitor",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "registry-storage",
    "secrets-namespace",
    "support",
}


def check_patched_pricing_rule_detail_request_product_kind_type_2_type_1(
    value: str,
) -> PatchedPricingRuleDetailRequestProductKindType2Type1:
    if value in PATCHED_PRICING_RULE_DETAIL_REQUEST_PRODUCT_KIND_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_RULE_DETAIL_REQUEST_PRODUCT_KIND_TYPE_2_TYPE_1_VALUES!r}"
    )
