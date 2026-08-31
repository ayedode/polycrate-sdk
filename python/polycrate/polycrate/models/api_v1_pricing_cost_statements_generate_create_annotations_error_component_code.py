from typing import Literal

ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_cost_statements_generate_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
