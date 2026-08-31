from typing import Literal

ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_cost_statements_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
