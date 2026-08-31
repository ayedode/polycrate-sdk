from typing import Literal

ApiV1PricingQuotesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quotes_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
