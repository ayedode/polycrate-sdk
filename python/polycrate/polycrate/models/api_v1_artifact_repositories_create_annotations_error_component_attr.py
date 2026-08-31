from typing import Literal

ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_artifact_repositories_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
