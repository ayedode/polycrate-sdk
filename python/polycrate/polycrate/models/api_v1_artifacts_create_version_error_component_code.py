from typing import Literal

ApiV1ArtifactsCreateVersionErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_ARTIFACTS_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateVersionErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_create_version_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateVersionErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
