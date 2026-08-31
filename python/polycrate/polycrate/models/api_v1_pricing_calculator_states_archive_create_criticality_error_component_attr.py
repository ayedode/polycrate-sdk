from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_calculator_states_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
