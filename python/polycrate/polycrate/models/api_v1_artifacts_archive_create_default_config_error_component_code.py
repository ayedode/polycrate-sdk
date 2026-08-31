from typing import Literal

ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_ARCHIVE_CREATE_DEFAULT_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_archive_create_default_config_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateDefaultConfigErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_DEFAULT_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_DEFAULT_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
