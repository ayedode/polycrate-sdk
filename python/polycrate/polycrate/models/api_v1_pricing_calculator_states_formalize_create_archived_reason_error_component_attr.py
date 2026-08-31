from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_pricing_calculator_states_formalize_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
