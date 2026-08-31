from typing import Literal

ApiV1PricingCostStatementsCreateCurrencyErrorComponentAttr = Literal["currency"]

API_V1_PRICING_COST_STATEMENTS_CREATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateCurrencyErrorComponentAttr
] = {
    "currency",
}


def check_api_v1_pricing_cost_statements_create_currency_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateCurrencyErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
