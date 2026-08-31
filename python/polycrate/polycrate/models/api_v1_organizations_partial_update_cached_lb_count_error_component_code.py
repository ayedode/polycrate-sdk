from typing import Literal

ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_LB_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_partial_update_cached_lb_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_LB_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_LB_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
