from typing import Literal

ApiV1PricingQuotesUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_QUOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_quotes_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
