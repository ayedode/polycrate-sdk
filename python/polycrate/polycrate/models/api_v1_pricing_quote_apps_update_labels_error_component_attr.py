from typing import Literal

ApiV1PricingQuoteAppsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_QUOTE_APPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_quote_apps_update_labels_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
