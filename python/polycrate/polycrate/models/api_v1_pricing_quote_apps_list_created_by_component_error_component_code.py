from typing import Literal

ApiV1PricingQuoteAppsListCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTE_APPS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsListCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_quote_apps_list_created_by_component_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsListCreatedByComponentErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
