from typing import Literal

ApiV1PricingRulesCreateActiveUntilErrorComponentAttr = Literal["active_until"]

API_V1_PRICING_RULES_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesCreateActiveUntilErrorComponentAttr
] = {
    "active_until",
}


def check_api_v1_pricing_rules_create_active_until_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateActiveUntilErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
