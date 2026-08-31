from typing import Literal

ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_organizations_update_cached_metrics_updated_at_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
