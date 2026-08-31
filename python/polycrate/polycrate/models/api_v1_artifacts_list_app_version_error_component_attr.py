from typing import Literal

ApiV1ArtifactsListAppVersionErrorComponentAttr = Literal["app_version"]

API_V1_ARTIFACTS_LIST_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsListAppVersionErrorComponentAttr] = {
    "app_version",
}


def check_api_v1_artifacts_list_app_version_error_component_attr(
    value: str,
) -> ApiV1ArtifactsListAppVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_LIST_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
