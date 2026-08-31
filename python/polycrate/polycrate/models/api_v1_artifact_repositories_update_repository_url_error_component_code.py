from typing import Literal

ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponentCode
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


def check_api_v1_artifact_repositories_update_repository_url_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
