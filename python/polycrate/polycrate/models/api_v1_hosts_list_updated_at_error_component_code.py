from typing import Literal

ApiV1HostsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_HOSTS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListUpdatedAtErrorComponentCode] = {
    "invalid",
}


def check_api_v1_hosts_list_updated_at_error_component_code(value: str) -> ApiV1HostsListUpdatedAtErrorComponentCode:
    if value in API_V1_HOSTS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
