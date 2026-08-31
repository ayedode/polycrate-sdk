from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_repositories_partial_update_tolerations_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateTolerationsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
