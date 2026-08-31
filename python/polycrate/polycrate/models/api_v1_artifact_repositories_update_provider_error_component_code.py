from typing import Literal

ApiV1ArtifactRepositoriesUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_artifact_repositories_update_provider_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateProviderErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
