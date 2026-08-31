from typing import Literal

ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_rules_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
