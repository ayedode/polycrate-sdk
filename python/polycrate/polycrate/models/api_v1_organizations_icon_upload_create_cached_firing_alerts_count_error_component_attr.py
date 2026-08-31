from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponentAttr = Literal["cached_firing_alerts_count"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponentAttr
] = {
    "cached_firing_alerts_count",
}


def check_api_v1_organizations_icon_upload_create_cached_firing_alerts_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
