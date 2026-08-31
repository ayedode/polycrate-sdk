from typing import Literal

ApiV1ArtifactsUpdatePrereleaseErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_UPDATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdatePrereleaseErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_update_prerelease_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdatePrereleaseErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_PRERELEASE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
