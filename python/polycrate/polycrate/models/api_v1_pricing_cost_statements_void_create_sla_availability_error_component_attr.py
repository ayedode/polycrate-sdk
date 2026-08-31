from typing import Literal

ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_cost_statements_void_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
