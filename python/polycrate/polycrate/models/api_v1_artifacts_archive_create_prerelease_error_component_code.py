from typing import Literal

ApiV1ArtifactsArchiveCreatePrereleaseErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreatePrereleaseErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_archive_create_prerelease_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreatePrereleaseErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
