from typing import Literal

ApiV1PricingCostStatementsVoidCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_cost_statements_void_create_labels_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateLabelsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
