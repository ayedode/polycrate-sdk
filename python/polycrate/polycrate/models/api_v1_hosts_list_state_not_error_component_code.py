from typing import Literal

ApiV1HostsListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_HOSTS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListStateNotErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_hosts_list_state_not_error_component_code(value: str) -> ApiV1HostsListStateNotErrorComponentCode:
    if value in API_V1_HOSTS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
