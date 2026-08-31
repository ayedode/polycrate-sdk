from typing import Literal

ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_PACKAGES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_packages_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
