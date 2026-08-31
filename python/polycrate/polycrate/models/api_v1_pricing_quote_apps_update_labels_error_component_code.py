from typing import Literal

ApiV1PricingQuoteAppsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTE_APPS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quote_apps_update_labels_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateLabelsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
