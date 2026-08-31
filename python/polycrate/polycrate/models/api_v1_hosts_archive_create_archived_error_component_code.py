from typing import Literal

ApiV1HostsArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1HostsArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
