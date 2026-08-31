from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_pricing_quote_apps_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
