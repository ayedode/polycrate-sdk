from typing import Literal

ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_pricing_cost_statements_void_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
