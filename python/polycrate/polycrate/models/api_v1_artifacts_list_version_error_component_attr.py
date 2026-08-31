from typing import Literal

ApiV1ArtifactsListVersionErrorComponentAttr = Literal["version"]

API_V1_ARTIFACTS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsListVersionErrorComponentAttr] = {
    "version",
}


def check_api_v1_artifacts_list_version_error_component_attr(value: str) -> ApiV1ArtifactsListVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
