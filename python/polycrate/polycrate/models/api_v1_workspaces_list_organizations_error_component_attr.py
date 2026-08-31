from typing import Literal

ApiV1WorkspacesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_WORKSPACES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_workspaces_list_organizations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesListOrganizationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
