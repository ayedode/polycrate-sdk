from typing import Literal

ApiV1PricingQuoteAppsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTE_APPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quote_apps_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
