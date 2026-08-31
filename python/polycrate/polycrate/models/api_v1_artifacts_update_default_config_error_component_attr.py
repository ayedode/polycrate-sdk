from typing import Literal

ApiV1ArtifactsUpdateDefaultConfigErrorComponentAttr = Literal["default_config"]

API_V1_ARTIFACTS_UPDATE_DEFAULT_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateDefaultConfigErrorComponentAttr
] = {
    "default_config",
}


def check_api_v1_artifacts_update_default_config_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateDefaultConfigErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_DEFAULT_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_DEFAULT_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
