from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_artifact_repositories_archive_create_repository_url_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
