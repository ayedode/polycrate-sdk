from typing import Literal

ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponentAttr = Literal["cached_metrics_30d_avg"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponentAttr
] = {
    "cached_metrics_30d_avg",
}


def check_api_v1_organizations_partial_update_cached_metrics_30d_avg_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
