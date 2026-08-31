from typing import Literal

ApiV1ArtifactPackagesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_PACKAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_packages_create_annotations_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesCreateAnnotationsErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
