from typing import Literal

ApiV1ArtifactsListArtifactPackageErrorComponentAttr = Literal["artifact_package"]

API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsListArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_api_v1_artifacts_list_artifact_package_error_component_attr(
    value: str,
) -> ApiV1ArtifactsListArtifactPackageErrorComponentAttr:
    if value in API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
