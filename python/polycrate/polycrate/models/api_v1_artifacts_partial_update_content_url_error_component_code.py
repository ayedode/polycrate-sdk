from typing import Literal

ApiV1ArtifactsPartialUpdateContentUrlErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_ARTIFACTS_PARTIAL_UPDATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateContentUrlErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_partial_update_content_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateContentUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_CONTENT_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
