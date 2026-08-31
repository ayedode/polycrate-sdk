from typing import Literal

ApiV1HostsArchiveCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_HOSTS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsArchiveCreateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1_hosts_archive_create_alias_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateAliasErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
