from typing import Literal

PricingRuleDetailProductKindType3Type1 = Literal[
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

PRICING_RULE_DETAIL_PRODUCT_KIND_TYPE_3_TYPE_1_VALUES: set[PricingRuleDetailProductKindType3Type1] = {
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


def check_pricing_rule_detail_product_kind_type_3_type_1(value: str) -> PricingRuleDetailProductKindType3Type1:
    if value in PRICING_RULE_DETAIL_PRODUCT_KIND_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_PRODUCT_KIND_TYPE_3_TYPE_1_VALUES!r}"
    )
