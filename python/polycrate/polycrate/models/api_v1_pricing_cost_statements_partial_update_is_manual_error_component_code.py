from typing import Literal

ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_partial_update_is_manual_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
