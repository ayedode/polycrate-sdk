from typing import Literal

ApiV1RegionsPartialUpdateConditionsErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateConditionsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_regions_partial_update_conditions_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateConditionsErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
