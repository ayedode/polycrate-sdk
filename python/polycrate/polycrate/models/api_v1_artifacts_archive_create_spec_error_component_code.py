from typing import Literal

ApiV1ArtifactsArchiveCreateSpecErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_ARCHIVE_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateSpecErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_archive_create_spec_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateSpecErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
