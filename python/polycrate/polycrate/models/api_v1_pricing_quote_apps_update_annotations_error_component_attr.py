from typing import Literal

ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTE_APPS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quote_apps_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
