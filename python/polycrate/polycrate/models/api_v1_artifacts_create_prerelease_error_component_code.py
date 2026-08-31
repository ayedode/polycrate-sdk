from typing import Literal

ApiV1ArtifactsCreatePrereleaseErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_CREATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsCreatePrereleaseErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_create_prerelease_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreatePrereleaseErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
