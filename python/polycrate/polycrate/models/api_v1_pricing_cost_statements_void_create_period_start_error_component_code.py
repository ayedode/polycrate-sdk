from typing import Literal

ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PERIOD_START_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_pricing_cost_statements_void_create_period_start_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PERIOD_START_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PERIOD_START_ERROR_COMPONENT_CODE_VALUES!r}"
    )
