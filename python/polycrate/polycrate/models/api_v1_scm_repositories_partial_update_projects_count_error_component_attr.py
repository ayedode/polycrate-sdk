from typing import Literal

ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponentAttr = Literal["projects_count"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponentAttr
] = {
    "projects_count",
}


def check_api_v1_scm_repositories_partial_update_projects_count_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
