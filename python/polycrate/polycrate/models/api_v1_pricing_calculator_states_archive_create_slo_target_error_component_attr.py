from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pricing_calculator_states_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
