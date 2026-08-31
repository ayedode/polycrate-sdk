from typing import Literal

ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_packages_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
