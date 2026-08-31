from typing import Literal

ApiV1ArtifactPackagesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_PACKAGES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_packages_create_criticality_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesCreateCriticalityErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
