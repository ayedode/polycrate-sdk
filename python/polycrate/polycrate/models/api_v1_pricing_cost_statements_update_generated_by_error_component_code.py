from typing import Literal

ApiV1PricingCostStatementsUpdateGeneratedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsUpdateGeneratedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_cost_statements_update_generated_by_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsUpdateGeneratedByErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
