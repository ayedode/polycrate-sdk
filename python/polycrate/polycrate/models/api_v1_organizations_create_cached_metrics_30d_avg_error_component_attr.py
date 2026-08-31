from typing import Literal

ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponentAttr = Literal["cached_metrics_30d_avg"]

API_V1_ORGANIZATIONS_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponentAttr
] = {
    "cached_metrics_30d_avg",
}


def check_api_v1_organizations_create_cached_metrics_30d_avg_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
