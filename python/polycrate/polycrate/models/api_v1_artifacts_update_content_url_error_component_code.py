from typing import Literal

ApiV1ArtifactsUpdateContentUrlErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_ARTIFACTS_UPDATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateContentUrlErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_update_content_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateContentUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
