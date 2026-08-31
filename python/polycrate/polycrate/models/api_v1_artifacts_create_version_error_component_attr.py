from typing import Literal

ApiV1ArtifactsCreateVersionErrorComponentAttr = Literal["version"]

API_V1_ARTIFACTS_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_artifacts_create_version_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
