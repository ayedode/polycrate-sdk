from typing import Literal

ApiV1OrganizationsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_ORGANIZATIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_organizations_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1OrganizationsListWorkspacesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
