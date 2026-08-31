from typing import Literal

ApiV1ArtifactsListArtifactPackageNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsListArtifactPackageNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_artifacts_list_artifact_package_name_error_component_code(
    value: str,
) -> ApiV1ArtifactsListArtifactPackageNameErrorComponentCode:
    if value in API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
