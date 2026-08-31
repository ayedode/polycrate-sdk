from typing import Literal

ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_cost_statements_generate_create_criticality_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
