from typing import Literal

ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pricing_cost_statements_void_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
