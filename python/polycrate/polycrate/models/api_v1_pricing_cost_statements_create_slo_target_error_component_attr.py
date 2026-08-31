from typing import Literal

ApiV1PricingCostStatementsCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PRICING_COST_STATEMENTS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pricing_cost_statements_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateSloTargetErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
