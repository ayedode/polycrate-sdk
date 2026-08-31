from typing import Literal

ApiV1RegionsListPlatformFeaturesErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_REGIONS_LIST_PLATFORM_FEATURES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsListPlatformFeaturesErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_regions_list_platform_features_error_component_code(
    value: str,
) -> ApiV1RegionsListPlatformFeaturesErrorComponentCode:
    if value in API_V1_REGIONS_LIST_PLATFORM_FEATURES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_PLATFORM_FEATURES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
