from typing import Literal

ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_pricing_cost_statements_generate_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
