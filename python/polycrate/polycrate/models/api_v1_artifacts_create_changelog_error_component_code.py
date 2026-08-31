from typing import Literal

ApiV1ArtifactsCreateChangelogErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_CREATE_CHANGELOG_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateChangelogErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_create_changelog_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateChangelogErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_CHANGELOG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_CHANGELOG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
