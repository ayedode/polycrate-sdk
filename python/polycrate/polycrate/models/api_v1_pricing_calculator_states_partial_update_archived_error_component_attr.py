from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_calculator_states_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
