from typing import Literal

ApiV1PricingQuotesListScopeErrorComponentAttr = Literal["scope"]

API_V1_PRICING_QUOTES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingQuotesListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_pricing_quotes_list_scope_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesListScopeErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
