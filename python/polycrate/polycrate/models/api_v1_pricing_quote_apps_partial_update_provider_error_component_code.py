from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quote_apps_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
