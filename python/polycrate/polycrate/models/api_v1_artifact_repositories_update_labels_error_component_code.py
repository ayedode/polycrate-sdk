from typing import Literal

ApiV1ArtifactRepositoriesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_repositories_update_labels_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateLabelsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
