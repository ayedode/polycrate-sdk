from typing import Literal

ApiV1PricingQuoteAppsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTE_APPS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quote_apps_update_kind_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateKindErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
