from typing import Literal

ApiV1PricingCostStatementsCreateIsManualErrorComponentAttr = Literal["is_manual"]

API_V1_PRICING_COST_STATEMENTS_CREATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateIsManualErrorComponentAttr
] = {
    "is_manual",
}


def check_api_v1_pricing_cost_statements_create_is_manual_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateIsManualErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
