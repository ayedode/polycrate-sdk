from typing import Literal

ApiV1PricingCostStatementsUpdateIsManualErrorComponentAttr = Literal["is_manual"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateIsManualErrorComponentAttr
] = {
    "is_manual",
}


def check_api_v1_pricing_cost_statements_update_is_manual_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateIsManualErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
