from typing import Literal

ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponentAttr = Literal["repository_version"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponentAttr
] = {
    "repository_version",
}


def check_api_v1_scm_repositories_archive_create_repository_version_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
