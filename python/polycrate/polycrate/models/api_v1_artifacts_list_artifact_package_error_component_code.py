from typing import Literal

ApiV1ArtifactsListArtifactPackageErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsListArtifactPackageErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifacts_list_artifact_package_error_component_code(
    value: str,
) -> ApiV1ArtifactsListArtifactPackageErrorComponentCode:
    if value in API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
