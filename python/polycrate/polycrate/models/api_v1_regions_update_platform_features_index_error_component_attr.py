from typing import Literal

ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponentAttr = Literal["platform_features.INDEX"]

API_V1_REGIONS_UPDATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponentAttr
] = {
    "platform_features.INDEX",
}


def check_api_v1_regions_update_platform_features_index_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
