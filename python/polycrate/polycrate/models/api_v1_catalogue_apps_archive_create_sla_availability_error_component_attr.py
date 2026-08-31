from typing import Literal

ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_catalogue_apps_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
