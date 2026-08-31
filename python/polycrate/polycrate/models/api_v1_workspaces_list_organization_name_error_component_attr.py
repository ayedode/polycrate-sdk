from typing import Literal

ApiV1WorkspacesListOrganizationNameErrorComponentAttr = Literal["organization_name"]

API_V1_WORKSPACES_LIST_ORGANIZATION_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesListOrganizationNameErrorComponentAttr
] = {
    "organization_name",
}


def check_api_v1_workspaces_list_organization_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesListOrganizationNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_LIST_ORGANIZATION_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_ORGANIZATION_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
