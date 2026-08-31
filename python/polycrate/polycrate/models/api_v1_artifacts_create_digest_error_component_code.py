from typing import Literal

ApiV1ArtifactsCreateDigestErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_CREATE_DIGEST_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateDigestErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_create_digest_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateDigestErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_DIGEST_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_DIGEST_ERROR_COMPONENT_CODE_VALUES!r}"
    )
