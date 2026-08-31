from typing import Literal

ApiV1ArtifactsUpdateVersionErrorComponentAttr = Literal["version"]

API_V1_ARTIFACTS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_artifacts_update_version_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
