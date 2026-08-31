from typing import Literal

ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponentAttr = Literal["currency"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponentAttr
] = {
    "currency",
}


def check_api_v1_pricing_cost_statements_generate_create_currency_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CURRENCY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
