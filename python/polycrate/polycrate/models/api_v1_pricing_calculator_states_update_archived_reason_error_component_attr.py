from typing import Literal

ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_pricing_calculator_states_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
