from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_artifact_repositories_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
