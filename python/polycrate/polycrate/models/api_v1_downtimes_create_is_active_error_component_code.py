from typing import Literal

ApiV1DowntimesCreateIsActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_CREATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesCreateIsActiveErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_create_is_active_error_component_code(
    value: str,
) -> ApiV1DowntimesCreateIsActiveErrorComponentCode:
    if value in API_V1_DOWNTIMES_CREATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
