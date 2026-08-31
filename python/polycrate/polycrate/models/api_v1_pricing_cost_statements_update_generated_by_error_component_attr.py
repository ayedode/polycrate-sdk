from typing import Literal

ApiV1PricingCostStatementsUpdateGeneratedByErrorComponentAttr = Literal["generated_by"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateGeneratedByErrorComponentAttr
] = {
    "generated_by",
}


def check_api_v1_pricing_cost_statements_update_generated_by_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateGeneratedByErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
