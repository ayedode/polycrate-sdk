from typing import Literal

ApiV1HostsArchiveCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsArchiveCreateActiveErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_archive_create_active_error_component_code(
    value: str,
) -> ApiV1HostsArchiveCreateActiveErrorComponentCode:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
