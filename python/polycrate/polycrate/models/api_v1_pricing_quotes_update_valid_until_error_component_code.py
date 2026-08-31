from typing import Literal

ApiV1PricingQuotesUpdateValidUntilErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_QUOTES_UPDATE_VALID_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesUpdateValidUntilErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_quotes_update_valid_until_error_component_code(
    value: str,
) -> ApiV1PricingQuotesUpdateValidUntilErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_UPDATE_VALID_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_VALID_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
