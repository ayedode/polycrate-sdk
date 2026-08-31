from typing import Literal

ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponentAttr = Literal["repository_version"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_REPOSITORY_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponentAttr
] = {
    "repository_version",
}


def check_api_v1_scm_repositories_partial_update_repository_version_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_REPOSITORY_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_REPOSITORY_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
