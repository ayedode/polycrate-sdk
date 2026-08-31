from typing import Literal

ApiV1RegionsUpdatePlatformFeaturesErrorComponentCode = Literal["empty", "not_a_list", "null"]

API_V1_REGIONS_UPDATE_PLATFORM_FEATURES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsUpdatePlatformFeaturesErrorComponentCode
] = {
    "empty",
    "not_a_list",
    "null",
}


def check_api_v1_regions_update_platform_features_error_component_code(
    value: str,
) -> ApiV1RegionsUpdatePlatformFeaturesErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_PLATFORM_FEATURES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_PLATFORM_FEATURES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
