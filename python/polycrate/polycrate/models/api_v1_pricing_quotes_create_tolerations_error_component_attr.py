from typing import Literal

ApiV1PricingQuotesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_QUOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_quotes_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
