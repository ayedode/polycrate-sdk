from typing import Literal

ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_archive_create_cached_metrics_30d_avg_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_METRICS_30D_AVG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
