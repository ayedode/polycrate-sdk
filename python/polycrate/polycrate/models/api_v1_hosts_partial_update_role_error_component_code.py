from typing import Literal

ApiV1HostsPartialUpdateRoleErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_HOSTS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsPartialUpdateRoleErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_hosts_partial_update_role_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdateRoleErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
