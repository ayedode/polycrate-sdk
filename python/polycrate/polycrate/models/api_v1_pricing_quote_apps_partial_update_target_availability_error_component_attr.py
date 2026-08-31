from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_pricing_quote_apps_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
