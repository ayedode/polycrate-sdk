from typing import Literal

ApiV1ArtifactsUpdateAppVersionErrorComponentAttr = Literal["app_version"]

API_V1_ARTIFACTS_UPDATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateAppVersionErrorComponentAttr
] = {
    "app_version",
}


def check_api_v1_artifacts_update_app_version_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateAppVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
