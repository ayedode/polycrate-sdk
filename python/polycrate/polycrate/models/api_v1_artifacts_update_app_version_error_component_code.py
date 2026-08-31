from typing import Literal

ApiV1ArtifactsUpdateAppVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_UPDATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateAppVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_update_app_version_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateAppVersionErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
