from typing import Literal

ApiV1ArtifactsUpdateVersionErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_ARTIFACTS_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsUpdateVersionErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_update_version_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateVersionErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
