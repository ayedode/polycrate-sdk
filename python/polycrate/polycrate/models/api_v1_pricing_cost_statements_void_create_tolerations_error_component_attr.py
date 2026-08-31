from typing import Literal

ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_cost_statements_void_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
