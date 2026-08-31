from typing import Literal

ApiV1ArtifactPackagesListArtifactRepositoryErrorComponentAttr = Literal["artifact_repository"]

API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesListArtifactRepositoryErrorComponentAttr
] = {
    "artifact_repository",
}


def check_api_v1_artifact_packages_list_artifact_repository_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesListArtifactRepositoryErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
