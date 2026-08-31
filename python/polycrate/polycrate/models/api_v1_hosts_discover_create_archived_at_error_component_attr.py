from typing import Literal

ApiV1HostsDiscoverCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_HOSTS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_hosts_discover_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateArchivedAtErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
