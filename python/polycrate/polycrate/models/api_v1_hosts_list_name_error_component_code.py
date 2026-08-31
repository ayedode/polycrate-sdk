from typing import Literal

ApiV1HostsListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_HOSTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListNameErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_hosts_list_name_error_component_code(value: str) -> ApiV1HostsListNameErrorComponentCode:
    if value in API_V1_HOSTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
