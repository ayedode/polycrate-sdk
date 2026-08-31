from typing import Literal

ApiV1ArtifactPackagesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ARTIFACT_PACKAGES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_artifact_packages_create_labels_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateLabelsErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
