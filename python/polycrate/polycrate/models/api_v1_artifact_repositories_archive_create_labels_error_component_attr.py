from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_artifact_repositories_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
