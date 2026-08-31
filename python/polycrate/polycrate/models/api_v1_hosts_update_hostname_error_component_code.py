from typing import Literal

ApiV1HostsUpdateHostnameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsUpdateHostnameErrorComponentCode] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_update_hostname_error_component_code(value: str) -> ApiV1HostsUpdateHostnameErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
