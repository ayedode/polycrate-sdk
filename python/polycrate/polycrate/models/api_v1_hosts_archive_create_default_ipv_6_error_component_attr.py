from typing import Literal

ApiV1HostsArchiveCreateDefaultIpv6ErrorComponentAttr = Literal["default_ipv6"]

API_V1_HOSTS_ARCHIVE_CREATE_DEFAULT_IPV_6_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateDefaultIpv6ErrorComponentAttr
] = {
    "default_ipv6",
}


def check_api_v1_hosts_archive_create_default_ipv_6_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateDefaultIpv6ErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_DEFAULT_IPV_6_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_DEFAULT_IPV_6_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
