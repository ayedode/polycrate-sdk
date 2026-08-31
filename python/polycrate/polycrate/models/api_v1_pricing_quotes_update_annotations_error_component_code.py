from typing import Literal

ApiV1PricingQuotesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quotes_update_annotations_error_component_code(
    value: str,
) -> ApiV1PricingQuotesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
