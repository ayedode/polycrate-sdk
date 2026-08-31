from typing import Literal

ApiV1HostsCreateHostnameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsCreateHostnameErrorComponentCode] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_create_hostname_error_component_code(value: str) -> ApiV1HostsCreateHostnameErrorComponentCode:
    if value in API_V1_HOSTS_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
