from typing import Literal

ApiV1RegionsPartialUpdateStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGIONS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_regions_partial_update_state_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateStateErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
