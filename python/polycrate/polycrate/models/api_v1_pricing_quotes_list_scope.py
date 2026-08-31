from typing import Literal

ApiV1PricingQuotesListScope = Literal["system", "user"]

API_V1_PRICING_QUOTES_LIST_SCOPE_VALUES: set[ApiV1PricingQuotesListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_quotes_list_scope(value: str) -> ApiV1PricingQuotesListScope:
    if value in API_V1_PRICING_QUOTES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_SCOPE_VALUES!r}")
