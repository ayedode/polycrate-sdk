from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_pricing_calculator_states_formalize_create_archived_at_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
