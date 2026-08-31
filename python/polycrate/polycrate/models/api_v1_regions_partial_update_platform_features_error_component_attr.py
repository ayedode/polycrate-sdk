from typing import Literal

ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponentAttr = Literal["platform_features"]

API_V1_REGIONS_PARTIAL_UPDATE_PLATFORM_FEATURES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponentAttr
] = {
    "platform_features",
}


def check_api_v1_regions_partial_update_platform_features_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_PLATFORM_FEATURES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_PLATFORM_FEATURES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
