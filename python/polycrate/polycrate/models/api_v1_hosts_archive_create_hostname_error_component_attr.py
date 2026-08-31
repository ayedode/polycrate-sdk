from typing import Literal

ApiV1HostsArchiveCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_HOSTS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_hosts_archive_create_hostname_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateHostnameErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
