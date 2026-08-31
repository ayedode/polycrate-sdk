from typing import Literal

ApiV1PricingQuotesUpdateValidUntilErrorComponentAttr = Literal["valid_until"]

API_V1_PRICING_QUOTES_UPDATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdateValidUntilErrorComponentAttr
] = {
    "valid_until",
}


def check_api_v1_pricing_quotes_update_valid_until_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateValidUntilErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_VALID_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
