from typing import Literal

ApiV1ArtifactPackagesListArtifactRepositoryNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesListArtifactRepositoryNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_artifact_packages_list_artifact_repository_name_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesListArtifactRepositoryNameErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_LIST_ARTIFACT_REPOSITORY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
