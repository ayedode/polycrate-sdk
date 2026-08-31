from typing import Literal

ApiV1HostsArchiveCreateActiveErrorComponentAttr = Literal["active"]

API_V1_HOSTS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsArchiveCreateActiveErrorComponentAttr] = {
    "active",
}


def check_api_v1_hosts_archive_create_active_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateActiveErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
