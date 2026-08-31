from typing import Literal

ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quotes_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
