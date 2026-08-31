from typing import Literal

ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_repositories_update_criticality_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
