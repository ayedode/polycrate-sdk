from typing import Literal

ApiV1PricingQuotesListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PricingQuotesListScopeErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_pricing_quotes_list_scope_error_component_code(
    value: str,
) -> ApiV1PricingQuotesListScopeErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
