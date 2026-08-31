from typing import Literal

ApiV1PricingCalculatorStatesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_calculator_states_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
