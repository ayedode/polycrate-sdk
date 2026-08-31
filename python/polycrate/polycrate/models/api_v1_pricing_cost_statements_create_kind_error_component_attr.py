from typing import Literal

ApiV1PricingCostStatementsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_COST_STATEMENTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_cost_statements_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
