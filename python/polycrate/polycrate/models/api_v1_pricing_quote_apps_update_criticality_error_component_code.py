from typing import Literal

ApiV1PricingQuoteAppsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_quote_apps_update_criticality_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
