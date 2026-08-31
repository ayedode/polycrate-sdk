from typing import Literal

ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponentAttr = Literal["is_manual"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponentAttr
] = {
    "is_manual",
}


def check_api_v1_pricing_cost_statements_partial_update_is_manual_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
