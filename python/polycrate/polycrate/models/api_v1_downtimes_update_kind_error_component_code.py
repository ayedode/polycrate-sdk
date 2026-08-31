from typing import Literal

ApiV1DowntimesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOWNTIMES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_downtimes_update_kind_error_component_code(value: str) -> ApiV1DowntimesUpdateKindErrorComponentCode:
    if value in API_V1_DOWNTIMES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
