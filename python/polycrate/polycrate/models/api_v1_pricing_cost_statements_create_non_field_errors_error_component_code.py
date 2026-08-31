from typing import Literal

ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
