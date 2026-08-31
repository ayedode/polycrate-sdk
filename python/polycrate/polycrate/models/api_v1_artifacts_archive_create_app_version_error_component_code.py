from typing import Literal

ApiV1ArtifactsArchiveCreateAppVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_ARCHIVE_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateAppVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_archive_create_app_version_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateAppVersionErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
