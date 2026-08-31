from typing import Literal

ApiV1ProjectsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_PROJECTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_projects_list_organizations_error_component_attr(
    value: str,
) -> ApiV1ProjectsListOrganizationsErrorComponentAttr:
    if value in API_V1_PROJECTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
