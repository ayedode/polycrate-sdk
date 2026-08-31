from typing import Literal

ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponentAttr = Literal["cached_metrics_30d_avg"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponentAttr
] = {
    "cached_metrics_30d_avg",
}


def check_api_v1_organizations_update_cached_metrics_30d_avg_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
