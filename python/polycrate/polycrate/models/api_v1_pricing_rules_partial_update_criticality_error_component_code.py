from typing import Literal

ApiV1PricingRulesPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_rules_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1PricingRulesPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
