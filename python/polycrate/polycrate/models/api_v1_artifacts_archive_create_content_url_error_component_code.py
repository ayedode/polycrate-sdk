from typing import Literal

ApiV1ArtifactsArchiveCreateContentUrlErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_ARTIFACTS_ARCHIVE_CREATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateContentUrlErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_archive_create_content_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateContentUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
