from typing import Literal

ApiV1HostsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsCreateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_create_archived_error_component_code(value: str) -> ApiV1HostsCreateArchivedErrorComponentCode:
    if value in API_V1_HOSTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
