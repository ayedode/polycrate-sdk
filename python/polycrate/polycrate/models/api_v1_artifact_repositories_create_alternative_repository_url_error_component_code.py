from typing import Literal

ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACT_REPOSITORIES_CREATE_ALTERNATIVE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifact_repositories_create_alternative_repository_url_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_ALTERNATIVE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_ALTERNATIVE_REPOSITORY_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
