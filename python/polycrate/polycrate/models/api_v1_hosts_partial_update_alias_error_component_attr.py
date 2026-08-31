from typing import Literal

ApiV1HostsPartialUpdateAliasErrorComponentAttr = Literal["alias"]

API_V1_HOSTS_PARTIAL_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsPartialUpdateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1_hosts_partial_update_alias_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateAliasErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
