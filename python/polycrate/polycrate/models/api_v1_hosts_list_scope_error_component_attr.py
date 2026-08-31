from typing import Literal

ApiV1HostsListScopeErrorComponentAttr = Literal["scope"]

API_V1_HOSTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_hosts_list_scope_error_component_attr(value: str) -> ApiV1HostsListScopeErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
