from typing import Literal

ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_quote_apps_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
