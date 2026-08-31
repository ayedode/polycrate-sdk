from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
