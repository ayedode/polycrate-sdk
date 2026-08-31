from typing import Literal

ApiV1ArtifactsUpdateReadmeMdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_UPDATE_README_MD_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsUpdateReadmeMdErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_update_readme_md_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateReadmeMdErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_README_MD_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_README_MD_ERROR_COMPONENT_CODE_VALUES!r}"
    )
