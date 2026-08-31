from typing import Literal

ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponentAttr = Literal["platform_features"]

API_V1_REGIONS_ARCHIVE_CREATE_PLATFORM_FEATURES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponentAttr
] = {
    "platform_features",
}


def check_api_v1_regions_archive_create_platform_features_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_PLATFORM_FEATURES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_PLATFORM_FEATURES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
