from typing import Literal

ApiV1DowntimesListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_DOWNTIMES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesListStateNotErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_downtimes_list_state_not_error_component_code(
    value: str,
) -> ApiV1DowntimesListStateNotErrorComponentCode:
    if value in API_V1_DOWNTIMES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
