from typing import Literal

ApiV1ArtifactsUpdateDeprecatedErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_UPDATE_DEPRECATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateDeprecatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_update_deprecated_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateDeprecatedErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_DEPRECATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_DEPRECATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
