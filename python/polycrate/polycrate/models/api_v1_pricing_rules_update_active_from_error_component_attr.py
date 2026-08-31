from typing import Literal

ApiV1PricingRulesUpdateActiveFromErrorComponentAttr = Literal["active_from"]

API_V1_PRICING_RULES_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesUpdateActiveFromErrorComponentAttr
] = {
    "active_from",
}


def check_api_v1_pricing_rules_update_active_from_error_component_attr(
    value: str,
) -> ApiV1PricingRulesUpdateActiveFromErrorComponentAttr:
    if value in API_V1_PRICING_RULES_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
