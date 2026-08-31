from typing import Literal

ApiV1PricingQuoteAppsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_quote_apps_create_criticality_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsCreateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
