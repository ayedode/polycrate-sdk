from typing import Literal

ApiV1ArtifactsArchiveCreateChangelogErrorComponentAttr = Literal["changelog"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateChangelogErrorComponentAttr
] = {
    "changelog",
}


def check_api_v1_artifacts_archive_create_changelog_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateChangelogErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
