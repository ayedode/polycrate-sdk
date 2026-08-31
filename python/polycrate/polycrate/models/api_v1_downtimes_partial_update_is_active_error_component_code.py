from typing import Literal

ApiV1DowntimesPartialUpdateIsActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesPartialUpdateIsActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_partial_update_is_active_error_component_code(
    value: str,
) -> ApiV1DowntimesPartialUpdateIsActiveErrorComponentCode:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
