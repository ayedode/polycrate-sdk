from typing import Literal

ApiV1ArtifactsPartialUpdateVersionErrorComponentAttr = Literal["version"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_artifacts_partial_update_version_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
