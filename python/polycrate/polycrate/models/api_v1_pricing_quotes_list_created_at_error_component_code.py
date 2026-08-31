from typing import Literal

ApiV1PricingQuotesListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quotes_list_created_at_error_component_code(
    value: str,
) -> ApiV1PricingQuotesListCreatedAtErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
