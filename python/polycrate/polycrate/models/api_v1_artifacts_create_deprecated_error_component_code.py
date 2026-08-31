from typing import Literal

ApiV1ArtifactsCreateDeprecatedErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_CREATE_DEPRECATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsCreateDeprecatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_create_deprecated_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateDeprecatedErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_DEPRECATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_DEPRECATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
