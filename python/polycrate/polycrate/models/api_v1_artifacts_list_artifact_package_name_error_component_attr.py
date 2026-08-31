from typing import Literal

ApiV1ArtifactsListArtifactPackageNameErrorComponentAttr = Literal["artifact_package_name"]

API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsListArtifactPackageNameErrorComponentAttr
] = {
    "artifact_package_name",
}


def check_api_v1_artifacts_list_artifact_package_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactsListArtifactPackageNameErrorComponentAttr:
    if value in API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_ARTIFACT_PACKAGE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
