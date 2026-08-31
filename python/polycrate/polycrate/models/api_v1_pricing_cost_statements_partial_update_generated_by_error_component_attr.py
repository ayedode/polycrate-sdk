from typing import Literal

ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponentAttr = Literal["generated_by"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponentAttr
] = {
    "generated_by",
}


def check_api_v1_pricing_cost_statements_partial_update_generated_by_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
