from typing import Literal

ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_cost_statements_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
