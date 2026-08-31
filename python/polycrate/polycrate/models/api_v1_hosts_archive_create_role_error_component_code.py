from typing import Literal

ApiV1HostsArchiveCreateRoleErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_HOSTS_ARCHIVE_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsArchiveCreateRoleErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_hosts_archive_create_role_error_component_code(
    value: str,
) -> ApiV1HostsArchiveCreateRoleErrorComponentCode:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
