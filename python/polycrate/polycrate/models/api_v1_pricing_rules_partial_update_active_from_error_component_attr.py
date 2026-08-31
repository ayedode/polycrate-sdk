from typing import Literal

ApiV1PricingRulesPartialUpdateActiveFromErrorComponentAttr = Literal["active_from"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesPartialUpdateActiveFromErrorComponentAttr
] = {
    "active_from",
}


def check_api_v1_pricing_rules_partial_update_active_from_error_component_attr(
    value: str,
) -> ApiV1PricingRulesPartialUpdateActiveFromErrorComponentAttr:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
