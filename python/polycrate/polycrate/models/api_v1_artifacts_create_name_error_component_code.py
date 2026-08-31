from typing import Literal

ApiV1ArtifactsCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_create_name_error_component_code(value: str) -> ApiV1ArtifactsCreateNameErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
