from typing import Literal

ApiV1ArtifactsArchiveCreateVersionErrorComponentAttr = Literal["version"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_artifacts_archive_create_version_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
