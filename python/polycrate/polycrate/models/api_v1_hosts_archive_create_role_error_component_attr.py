from typing import Literal

ApiV1HostsArchiveCreateRoleErrorComponentAttr = Literal["role"]

API_V1_HOSTS_ARCHIVE_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsArchiveCreateRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_hosts_archive_create_role_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateRoleErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
