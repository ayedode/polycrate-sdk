from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_ACCESS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_pricing_calculator_states_archive_create_access_count_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_ACCESS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_ACCESS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
