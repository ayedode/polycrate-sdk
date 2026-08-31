from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_loadbalancers_regions_archive_create_region_name_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
