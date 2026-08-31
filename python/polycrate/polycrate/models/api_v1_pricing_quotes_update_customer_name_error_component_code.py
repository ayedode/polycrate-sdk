from typing import Literal

ApiV1PricingQuotesUpdateCustomerNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_QUOTES_UPDATE_CUSTOMER_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesUpdateCustomerNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_quotes_update_customer_name_error_component_code(
    value: str,
) -> ApiV1PricingQuotesUpdateCustomerNameErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_UPDATE_CUSTOMER_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_CUSTOMER_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
