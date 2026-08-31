from typing import Literal

ApiV1PricingQuoteAppsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTE_APPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quote_apps_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
