from typing import Literal

ApiV1PricingRulesCreateActiveUntilErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_RULES_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesCreateActiveUntilErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_rules_create_active_until_error_component_code(
    value: str,
) -> ApiV1PricingRulesCreateActiveUntilErrorComponentCode:
    if value in API_V1_PRICING_RULES_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
