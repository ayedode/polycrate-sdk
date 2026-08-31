from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_calculator_states_formalize_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
