from typing import Literal

ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_quotes_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
