from typing import Literal

ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_repositories_create_annotations_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
