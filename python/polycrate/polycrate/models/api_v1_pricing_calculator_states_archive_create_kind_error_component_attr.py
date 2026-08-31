from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_calculator_states_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
