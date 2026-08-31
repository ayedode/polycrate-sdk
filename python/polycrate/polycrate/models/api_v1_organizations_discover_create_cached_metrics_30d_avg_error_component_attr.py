from typing import Literal

ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponentAttr = Literal["cached_metrics_30d_avg"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponentAttr
] = {
    "cached_metrics_30d_avg",
}


def check_api_v1_organizations_discover_create_cached_metrics_30d_avg_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
