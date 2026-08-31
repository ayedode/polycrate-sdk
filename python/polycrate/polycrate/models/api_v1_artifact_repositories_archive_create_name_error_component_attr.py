from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_artifact_repositories_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
