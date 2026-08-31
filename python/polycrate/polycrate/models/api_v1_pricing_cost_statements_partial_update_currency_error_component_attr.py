from typing import Literal

ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponentAttr = Literal["currency"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponentAttr
] = {
    "currency",
}


def check_api_v1_pricing_cost_statements_partial_update_currency_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
