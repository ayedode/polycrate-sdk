from typing import Literal

ApiV1ArtifactsPartialUpdateAppVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_PARTIAL_UPDATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateAppVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_partial_update_app_version_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateAppVersionErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
