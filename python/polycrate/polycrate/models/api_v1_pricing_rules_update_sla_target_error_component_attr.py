from typing import Literal

ApiV1PricingRulesUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_RULES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_rules_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingRulesUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_RULES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
