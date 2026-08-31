from typing import Literal

ApiV1HostsUpdateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsUpdateActiveErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_update_active_error_component_code(value: str) -> ApiV1HostsUpdateActiveErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
