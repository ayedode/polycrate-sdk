from typing import Literal

ApiV1ArtifactPackagesListArtifactRepositoryNameErrorComponentAttr = Literal["artifact_repository_name"]

API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesListArtifactRepositoryNameErrorComponentAttr
] = {
    "artifact_repository_name",
}


def check_api_v1_artifact_packages_list_artifact_repository_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesListArtifactRepositoryNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
