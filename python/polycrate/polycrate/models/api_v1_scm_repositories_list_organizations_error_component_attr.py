from typing import Literal

ApiV1ScmRepositoriesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_SCM_REPOSITORIES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_scm_repositories_list_organizations_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesListOrganizationsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
