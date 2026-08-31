from typing import Literal

ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_archive_create_mirrored_content_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateMirroredContentUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
