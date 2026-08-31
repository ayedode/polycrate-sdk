from typing import Literal

ApiV1PricingQuotesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_QUOTES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_quotes_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
