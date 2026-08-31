from typing import Literal

ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_UPDATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_update_cached_firing_alerts_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
