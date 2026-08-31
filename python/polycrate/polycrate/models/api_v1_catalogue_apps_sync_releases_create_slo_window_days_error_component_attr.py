from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_catalogue_apps_sync_releases_create_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
