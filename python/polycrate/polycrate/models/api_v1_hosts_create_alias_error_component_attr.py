from typing import Literal

ApiV1HostsCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_HOSTS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1_hosts_create_alias_error_component_attr(value: str) -> ApiV1HostsCreateAliasErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
