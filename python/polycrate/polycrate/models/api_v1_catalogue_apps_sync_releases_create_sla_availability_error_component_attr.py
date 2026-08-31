from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_catalogue_apps_sync_releases_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
