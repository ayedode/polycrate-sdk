from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_organizations_discover_create_cached_metrics_updated_at_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
