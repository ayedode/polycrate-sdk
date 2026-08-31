from typing import Literal

ApiV1PricingQuoteAppsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_QUOTE_APPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_quote_apps_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
