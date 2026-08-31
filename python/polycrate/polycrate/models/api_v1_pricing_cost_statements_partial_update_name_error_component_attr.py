from typing import Literal

ApiV1PricingCostStatementsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_cost_statements_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
