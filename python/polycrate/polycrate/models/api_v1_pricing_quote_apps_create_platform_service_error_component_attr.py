from typing import Literal

ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_QUOTE_APPS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_quote_apps_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
