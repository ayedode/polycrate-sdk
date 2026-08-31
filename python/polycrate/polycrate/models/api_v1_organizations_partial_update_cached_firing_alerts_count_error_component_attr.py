from typing import Literal

ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponentAttr = Literal["cached_firing_alerts_count"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponentAttr
] = {
    "cached_firing_alerts_count",
}


def check_api_v1_organizations_partial_update_cached_firing_alerts_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
