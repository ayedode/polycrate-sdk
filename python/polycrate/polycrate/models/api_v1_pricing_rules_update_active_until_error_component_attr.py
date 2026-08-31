from typing import Literal

ApiV1PricingRulesUpdateActiveUntilErrorComponentAttr = Literal["active_until"]

API_V1_PRICING_RULES_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesUpdateActiveUntilErrorComponentAttr
] = {
    "active_until",
}


def check_api_v1_pricing_rules_update_active_until_error_component_attr(
    value: str,
) -> ApiV1PricingRulesUpdateActiveUntilErrorComponentAttr:
    if value in API_V1_PRICING_RULES_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
