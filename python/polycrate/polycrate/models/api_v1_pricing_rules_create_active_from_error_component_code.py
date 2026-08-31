from typing import Literal

ApiV1PricingRulesCreateActiveFromErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_RULES_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesCreateActiveFromErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_rules_create_active_from_error_component_code(
    value: str,
) -> ApiV1PricingRulesCreateActiveFromErrorComponentCode:
    if value in API_V1_PRICING_RULES_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
