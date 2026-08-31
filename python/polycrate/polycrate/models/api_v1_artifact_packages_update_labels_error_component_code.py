from typing import Literal

ApiV1ArtifactPackagesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_PACKAGES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_packages_update_labels_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesUpdateLabelsErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
