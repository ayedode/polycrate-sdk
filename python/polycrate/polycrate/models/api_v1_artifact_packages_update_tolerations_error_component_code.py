from typing import Literal

ApiV1ArtifactPackagesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_update_tolerations_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesUpdateTolerationsErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
