from typing import Literal

ApiV1ArtifactsCreatePrereleaseErrorComponentAttr = Literal["prerelease"]

API_V1_ARTIFACTS_CREATE_PRERELEASE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsCreatePrereleaseErrorComponentAttr
] = {
    "prerelease",
}


def check_api_v1_artifacts_create_prerelease_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreatePrereleaseErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_PRERELEASE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_PRERELEASE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
