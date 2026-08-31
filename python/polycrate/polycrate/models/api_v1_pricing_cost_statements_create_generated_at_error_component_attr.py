from typing import Literal

ApiV1PricingCostStatementsCreateGeneratedAtErrorComponentAttr = Literal["generated_at"]

API_V1_PRICING_COST_STATEMENTS_CREATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateGeneratedAtErrorComponentAttr
] = {
    "generated_at",
}


def check_api_v1_pricing_cost_statements_create_generated_at_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateGeneratedAtErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
