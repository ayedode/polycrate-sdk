from typing import Literal

ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_pricing_cost_statements_generate_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
