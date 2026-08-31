from typing import Literal

ApiV1PricingRulesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_RULES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_rules_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
