from typing import Literal

ApiV1PricingQuoteAppsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTE_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quote_apps_create_labels_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsCreateLabelsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
