from typing import Literal

ApiV1ArtifactRepositoriesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_artifact_repositories_update_labels_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateLabelsErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
