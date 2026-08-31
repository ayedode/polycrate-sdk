from typing import Literal

ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow", "required"
]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
    "required",
}


def check_api_v1_pricing_cost_statements_generate_create_period_end_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_CODE_VALUES!r}"
    )
