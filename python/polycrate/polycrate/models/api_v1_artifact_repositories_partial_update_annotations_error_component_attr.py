from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_artifact_repositories_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
