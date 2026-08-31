from typing import Literal

ApiV1ArtifactsCreateContentUrlErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_ARTIFACTS_CREATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsCreateContentUrlErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_create_content_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateContentUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
