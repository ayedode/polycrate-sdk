from typing import Literal

ApiV1PricingQuoteAppsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_apps_create_archived_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsCreateArchivedErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
