from typing import Literal

ApiV1ArtifactsPartialUpdateAppVersionErrorComponentAttr = Literal["app_version"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateAppVersionErrorComponentAttr
] = {
    "app_version",
}


def check_api_v1_artifacts_partial_update_app_version_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateAppVersionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_APP_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
