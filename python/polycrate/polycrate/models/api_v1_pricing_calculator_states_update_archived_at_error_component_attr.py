from typing import Literal

ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_calculator_states_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
