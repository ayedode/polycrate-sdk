from typing import Literal

ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PRICING_COST_STATEMENTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_pricing_cost_statements_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
