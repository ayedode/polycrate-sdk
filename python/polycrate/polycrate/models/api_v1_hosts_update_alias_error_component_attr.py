from typing import Literal

ApiV1HostsUpdateAliasErrorComponentAttr = Literal["alias"]

API_V1_HOSTS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1_hosts_update_alias_error_component_attr(value: str) -> ApiV1HostsUpdateAliasErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
