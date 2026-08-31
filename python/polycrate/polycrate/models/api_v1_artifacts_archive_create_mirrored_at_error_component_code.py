from typing import Literal

ApiV1ArtifactsArchiveCreateMirroredAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateMirroredAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_artifacts_archive_create_mirrored_at_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateMirroredAtErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
