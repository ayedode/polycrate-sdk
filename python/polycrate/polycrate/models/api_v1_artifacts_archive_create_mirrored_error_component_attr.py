from typing import Literal

ApiV1ArtifactsArchiveCreateMirroredErrorComponentAttr = Literal["mirrored"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateMirroredErrorComponentAttr
] = {
    "mirrored",
}


def check_api_v1_artifacts_archive_create_mirrored_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateMirroredErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
