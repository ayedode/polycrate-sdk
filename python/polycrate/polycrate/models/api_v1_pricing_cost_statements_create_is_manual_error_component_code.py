from typing import Literal

ApiV1PricingCostStatementsCreateIsManualErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsCreateIsManualErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_create_is_manual_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsCreateIsManualErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
