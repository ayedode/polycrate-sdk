from typing import Literal

ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_scm_repositories_archive_create_repository_version_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateRepositoryVersionErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
