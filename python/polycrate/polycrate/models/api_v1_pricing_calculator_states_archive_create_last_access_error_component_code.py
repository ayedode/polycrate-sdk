from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_LAST_ACCESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_pricing_calculator_states_archive_create_last_access_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_LAST_ACCESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_LAST_ACCESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
