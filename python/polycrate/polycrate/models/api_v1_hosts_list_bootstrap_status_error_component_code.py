from typing import Literal

ApiV1HostsListBootstrapStatusErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_HOSTS_LIST_BOOTSTRAP_STATUS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListBootstrapStatusErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_hosts_list_bootstrap_status_error_component_code(
    value: str,
) -> ApiV1HostsListBootstrapStatusErrorComponentCode:
    if value in API_V1_HOSTS_LIST_BOOTSTRAP_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_BOOTSTRAP_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
