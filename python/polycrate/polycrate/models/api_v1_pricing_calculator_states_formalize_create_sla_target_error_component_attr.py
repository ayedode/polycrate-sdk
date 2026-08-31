from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_calculator_states_formalize_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
