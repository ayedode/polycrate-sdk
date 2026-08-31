from typing import Literal

ApiV1PricingQuotesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PRICING_QUOTES_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1PricingQuotesListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pricing_quotes_list_created_by_component(value: str) -> ApiV1PricingQuotesListCreatedByComponent:
    if value in API_V1_PRICING_QUOTES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
