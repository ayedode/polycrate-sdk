from typing import Literal

ApiV1PricingQuotesListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PricingQuotesListKindErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_pricing_quotes_list_kind_error_component_code(
    value: str,
) -> ApiV1PricingQuotesListKindErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
