from typing import Literal

ApiV1PricingQuotesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quotes_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingQuotesCreateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
