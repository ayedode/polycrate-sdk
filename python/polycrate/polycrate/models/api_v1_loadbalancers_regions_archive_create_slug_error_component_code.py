from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed", "unique"
]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_loadbalancers_regions_archive_create_slug_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
