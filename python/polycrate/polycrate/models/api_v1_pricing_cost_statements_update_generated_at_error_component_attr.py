from typing import Literal

ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponentAttr = Literal["generated_at"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponentAttr
] = {
    "generated_at",
}


def check_api_v1_pricing_cost_statements_update_generated_at_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
