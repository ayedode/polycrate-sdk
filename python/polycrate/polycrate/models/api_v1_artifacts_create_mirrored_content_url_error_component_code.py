from typing import Literal

ApiV1ArtifactsCreateMirroredContentUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsCreateMirroredContentUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_create_mirrored_content_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateMirroredContentUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_MIRRORED_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
