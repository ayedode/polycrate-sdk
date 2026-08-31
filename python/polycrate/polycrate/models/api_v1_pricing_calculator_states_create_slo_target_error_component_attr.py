from typing import Literal

ApiV1PricingCalculatorStatesCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pricing_calculator_states_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateSloTargetErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
