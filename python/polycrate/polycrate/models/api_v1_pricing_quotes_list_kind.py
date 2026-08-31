from typing import Literal

ApiV1PricingQuotesListKind = Literal["generic"]

API_V1_PRICING_QUOTES_LIST_KIND_VALUES: set[ApiV1PricingQuotesListKind] = {
    "generic",
}


def check_api_v1_pricing_quotes_list_kind(value: str) -> ApiV1PricingQuotesListKind:
    if value in API_V1_PRICING_QUOTES_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_KIND_VALUES!r}")
