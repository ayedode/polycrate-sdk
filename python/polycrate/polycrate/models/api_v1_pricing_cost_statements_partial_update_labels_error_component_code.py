from typing import Literal

ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_cost_statements_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
