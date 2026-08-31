from typing import Literal

ApiV1ArtifactPackagesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ARTIFACT_PACKAGES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_artifact_packages_update_labels_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateLabelsErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
