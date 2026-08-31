from typing import Literal

ApiV1PricingRulesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PRICING_RULES_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1PricingRulesListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pricing_rules_list_created_by_component(value: str) -> ApiV1PricingRulesListCreatedByComponent:
    if value in API_V1_PRICING_RULES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
