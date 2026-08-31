from typing import Literal

ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
