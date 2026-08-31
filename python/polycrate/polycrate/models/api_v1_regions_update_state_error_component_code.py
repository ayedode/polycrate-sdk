from typing import Literal

ApiV1RegionsUpdateStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGIONS_UPDATE_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsUpdateStateErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_regions_update_state_error_component_code(value: str) -> ApiV1RegionsUpdateStateErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
