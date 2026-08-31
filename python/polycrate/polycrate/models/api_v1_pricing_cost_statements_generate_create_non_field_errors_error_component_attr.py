from typing import Literal

ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_pricing_cost_statements_generate_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
