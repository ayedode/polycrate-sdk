from typing import Literal

ApiV1PricingQuotesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_QUOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_quotes_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
