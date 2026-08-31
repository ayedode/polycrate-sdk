from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_artifact_repositories_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
