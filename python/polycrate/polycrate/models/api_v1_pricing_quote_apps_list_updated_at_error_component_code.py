from typing import Literal

ApiV1PricingQuoteAppsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quote_apps_list_updated_at_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsListUpdatedAtErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
