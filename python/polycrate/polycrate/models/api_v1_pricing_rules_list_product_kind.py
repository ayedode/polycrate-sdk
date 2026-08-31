from typing import Literal

ApiV1PricingRulesListProductKind = Literal[
    "assistant",
    "block-storage",
    "dnszone",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "support",
]

API_V1_PRICING_RULES_LIST_PRODUCT_KIND_VALUES: set[ApiV1PricingRulesListProductKind] = {
    "assistant",
    "block-storage",
    "dnszone",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "support",
}


def check_api_v1_pricing_rules_list_product_kind(value: str) -> ApiV1PricingRulesListProductKind:
    if value in API_V1_PRICING_RULES_LIST_PRODUCT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_PRODUCT_KIND_VALUES!r}")
