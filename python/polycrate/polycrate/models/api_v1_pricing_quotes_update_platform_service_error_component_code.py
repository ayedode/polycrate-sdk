from typing import Literal

ApiV1PricingQuotesUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quotes_update_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingQuotesUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
