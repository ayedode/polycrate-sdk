from typing import Literal

ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponentAttr = Literal["generated_by"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponentAttr
] = {
    "generated_by",
}


def check_api_v1_pricing_cost_statements_void_create_generated_by_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_GENERATED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
