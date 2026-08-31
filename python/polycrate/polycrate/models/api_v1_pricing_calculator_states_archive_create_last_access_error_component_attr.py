from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponentAttr = Literal["last_access"]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_LAST_ACCESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponentAttr
] = {
    "last_access",
}


def check_api_v1_pricing_calculator_states_archive_create_last_access_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_LAST_ACCESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_LAST_ACCESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
