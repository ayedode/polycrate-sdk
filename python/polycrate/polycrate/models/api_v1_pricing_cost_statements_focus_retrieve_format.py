from typing import Literal

ApiV1PricingCostStatementsFocusRetrieveFormat = Literal["csv", "json"]

API_V1_PRICING_COST_STATEMENTS_FOCUS_RETRIEVE_FORMAT_VALUES: set[ApiV1PricingCostStatementsFocusRetrieveFormat] = {
    "csv",
    "json",
}


def check_api_v1_pricing_cost_statements_focus_retrieve_format(
    value: str,
) -> ApiV1PricingCostStatementsFocusRetrieveFormat:
    if value in API_V1_PRICING_COST_STATEMENTS_FOCUS_RETRIEVE_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_FOCUS_RETRIEVE_FORMAT_VALUES!r}"
    )
