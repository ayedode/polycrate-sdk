from typing import Literal

ApiV1ScmRepositoriesCreateProjectsCountErrorComponentAttr = Literal["projects_count"]

API_V1_SCM_REPOSITORIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateProjectsCountErrorComponentAttr
] = {
    "projects_count",
}


def check_api_v1_scm_repositories_create_projects_count_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateProjectsCountErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
