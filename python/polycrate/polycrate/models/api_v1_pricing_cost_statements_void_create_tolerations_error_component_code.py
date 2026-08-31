from typing import Literal

ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_void_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
