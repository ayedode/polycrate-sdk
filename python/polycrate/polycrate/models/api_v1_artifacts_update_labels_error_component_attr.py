from typing import Literal

ApiV1ArtifactsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ARTIFACTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_artifacts_update_labels_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateLabelsErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
