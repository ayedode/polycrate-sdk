from typing import Literal

ApiV1PricingCostStatementsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_COST_STATEMENTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_cost_statements_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
