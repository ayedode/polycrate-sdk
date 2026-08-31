from typing import Literal

ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponentAttr = Literal["default_config"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_DEFAULT_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponentAttr
] = {
    "default_config",
}


def check_api_v1_artifacts_partial_update_default_config_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateDefaultConfigErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_DEFAULT_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_DEFAULT_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
