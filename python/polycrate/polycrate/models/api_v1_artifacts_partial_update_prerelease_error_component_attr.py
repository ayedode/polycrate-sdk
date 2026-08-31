from typing import Literal

ApiV1ArtifactsPartialUpdatePrereleaseErrorComponentAttr = Literal["prerelease"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_PRERELEASE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdatePrereleaseErrorComponentAttr
] = {
    "prerelease",
}


def check_api_v1_artifacts_partial_update_prerelease_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdatePrereleaseErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_PRERELEASE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_PRERELEASE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
