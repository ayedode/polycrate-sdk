from typing import Literal

ApiV1HostsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_HOSTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListCreatedAtErrorComponentCode] = {
    "invalid",
}


def check_api_v1_hosts_list_created_at_error_component_code(value: str) -> ApiV1HostsListCreatedAtErrorComponentCode:
    if value in API_V1_HOSTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
