from typing import Literal

ApiV1ArtifactsPartialUpdateSpecErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateSpecErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifacts_partial_update_spec_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateSpecErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
