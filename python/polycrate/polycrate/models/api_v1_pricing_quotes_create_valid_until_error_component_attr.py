from typing import Literal

ApiV1PricingQuotesCreateValidUntilErrorComponentAttr = Literal["valid_until"]

API_V1_PRICING_QUOTES_CREATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateValidUntilErrorComponentAttr
] = {
    "valid_until",
}


def check_api_v1_pricing_quotes_create_valid_until_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateValidUntilErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
