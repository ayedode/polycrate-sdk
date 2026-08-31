from typing import Literal

ApiV1IpaddressesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_IPADDRESSES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_ipaddresses_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1IpaddressesListWorkspacesErrorComponentAttr:
    if value in API_V1_IPADDRESSES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
