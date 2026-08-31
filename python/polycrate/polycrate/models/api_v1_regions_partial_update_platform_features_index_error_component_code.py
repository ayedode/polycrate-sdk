from typing import Literal

ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_REGIONS_PARTIAL_UPDATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_regions_partial_update_platform_features_index_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_PLATFORM_FEATURES_INDEX_ERROR_COMPONENT_CODE_VALUES!r}"
    )
