from typing import Literal

ApiV1ArtifactPackagesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesCreateTolerationsErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
