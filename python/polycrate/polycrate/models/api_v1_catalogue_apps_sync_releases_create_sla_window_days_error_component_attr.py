from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_catalogue_apps_sync_releases_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
