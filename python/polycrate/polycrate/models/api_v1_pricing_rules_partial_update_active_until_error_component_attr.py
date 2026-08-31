from typing import Literal

ApiV1PricingRulesPartialUpdateActiveUntilErrorComponentAttr = Literal["active_until"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesPartialUpdateActiveUntilErrorComponentAttr
] = {
    "active_until",
}


def check_api_v1_pricing_rules_partial_update_active_until_error_component_attr(
    value: str,
) -> ApiV1PricingRulesPartialUpdateActiveUntilErrorComponentAttr:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
