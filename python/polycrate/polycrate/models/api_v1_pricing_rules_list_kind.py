from typing import Literal

ApiV1PricingRulesListKind = Literal["generic"]

API_V1_PRICING_RULES_LIST_KIND_VALUES: set[ApiV1PricingRulesListKind] = {
    "generic",
}


def check_api_v1_pricing_rules_list_kind(value: str) -> ApiV1PricingRulesListKind:
    if value in API_V1_PRICING_RULES_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_KIND_VALUES!r}")
