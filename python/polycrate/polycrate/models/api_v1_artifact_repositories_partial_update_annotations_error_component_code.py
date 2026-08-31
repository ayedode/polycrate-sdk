from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_repositories_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
