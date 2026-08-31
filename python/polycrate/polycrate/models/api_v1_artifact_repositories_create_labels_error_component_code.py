from typing import Literal

ApiV1ArtifactRepositoriesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_repositories_create_labels_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateLabelsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
