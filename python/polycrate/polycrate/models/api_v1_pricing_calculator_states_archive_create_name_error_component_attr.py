from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_calculator_states_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
