from typing import Literal

ApiV1PricingCostStatementsPartialUpdateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_cost_statements_partial_update_status_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateStatusErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
