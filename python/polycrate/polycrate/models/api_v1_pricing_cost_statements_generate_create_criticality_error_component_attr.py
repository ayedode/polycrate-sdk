from typing import Literal

ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_cost_statements_generate_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
