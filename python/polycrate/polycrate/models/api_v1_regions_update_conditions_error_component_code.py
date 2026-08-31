from typing import Literal

ApiV1RegionsUpdateConditionsErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsUpdateConditionsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_regions_update_conditions_error_component_code(
    value: str,
) -> ApiV1RegionsUpdateConditionsErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
