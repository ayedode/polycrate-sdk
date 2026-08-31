from typing import Literal

ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_PARTIAL_UPDATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_partial_update_website_url_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateWebsiteUrlErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
