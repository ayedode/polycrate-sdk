from typing import Literal

ApiV1HostsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_HOSTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1_hosts_list_workspaces_error_component_attr(value: str) -> ApiV1HostsListWorkspacesErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
