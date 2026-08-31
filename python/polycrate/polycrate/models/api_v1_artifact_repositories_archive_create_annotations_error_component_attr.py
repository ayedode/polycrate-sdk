from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_artifact_repositories_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
