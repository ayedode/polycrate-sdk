from typing import Literal

ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_cost_statements_void_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
