from typing import Literal

ApiV1PricingRulesListStateErrorComponentAttr = Literal["state"]

API_V1_PRICING_RULES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_pricing_rules_list_state_error_component_attr(
    value: str,
) -> ApiV1PricingRulesListStateErrorComponentAttr:
    if value in API_V1_PRICING_RULES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
