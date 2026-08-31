from typing import Literal

ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_GENERATED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_cost_statements_partial_update_generated_by_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_GENERATED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_GENERATED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
