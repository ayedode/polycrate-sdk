from typing import Literal

ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponentAttr = Literal["platform_features.INDEX"]

API_V1_REGIONS_CREATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponentAttr
] = {
    "platform_features.INDEX",
}


def check_api_v1_regions_create_platform_features_index_error_component_attr(
    value: str,
) -> ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
