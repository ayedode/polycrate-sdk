from typing import Literal

ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CATALOGUE_APPS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_catalogue_apps_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
