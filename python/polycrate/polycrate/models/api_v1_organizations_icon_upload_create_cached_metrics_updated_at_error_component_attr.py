from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponentAttr = Literal["cached_metrics_updated_at"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponentAttr
] = {
    "cached_metrics_updated_at",
}


def check_api_v1_organizations_icon_upload_create_cached_metrics_updated_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_METRICS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
