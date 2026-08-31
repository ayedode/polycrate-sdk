from typing import Literal

ApiV1PricingQuotesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quotes_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingQuotesCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
