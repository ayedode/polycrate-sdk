from typing import Literal

ApiV1ArtifactsArchiveCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_artifacts_archive_create_metadata_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateMetadataErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
