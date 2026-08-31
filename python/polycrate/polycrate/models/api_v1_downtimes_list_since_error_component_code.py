from typing import Literal

ApiV1DowntimesListSinceErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesListSinceErrorComponentCode] = {
    "invalid",
}


def check_api_v1_downtimes_list_since_error_component_code(value: str) -> ApiV1DowntimesListSinceErrorComponentCode:
    if value in API_V1_DOWNTIMES_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_SINCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
