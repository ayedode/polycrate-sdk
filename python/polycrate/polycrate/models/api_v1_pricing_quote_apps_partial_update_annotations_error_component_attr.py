from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quote_apps_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
