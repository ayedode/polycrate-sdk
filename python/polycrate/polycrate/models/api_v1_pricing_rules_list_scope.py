from typing import Literal

ApiV1PricingRulesListScope = Literal["system", "user"]

API_V1_PRICING_RULES_LIST_SCOPE_VALUES: set[ApiV1PricingRulesListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_rules_list_scope(value: str) -> ApiV1PricingRulesListScope:
    if value in API_V1_PRICING_RULES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_SCOPE_VALUES!r}")
