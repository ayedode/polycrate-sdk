from typing import Literal

ApiV1HostsPartialUpdateHostnameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsPartialUpdateHostnameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_partial_update_hostname_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdateHostnameErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
