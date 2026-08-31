from typing import Literal

ApiV1RegionsPartialUpdateLastStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGIONS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateLastStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_regions_partial_update_last_state_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateLastStateErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
