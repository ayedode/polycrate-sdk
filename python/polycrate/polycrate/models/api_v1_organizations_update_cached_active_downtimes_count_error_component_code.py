from typing import Literal

ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_UPDATE_CACHED_ACTIVE_DOWNTIMES_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_update_cached_active_downtimes_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_ACTIVE_DOWNTIMES_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_ACTIVE_DOWNTIMES_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
