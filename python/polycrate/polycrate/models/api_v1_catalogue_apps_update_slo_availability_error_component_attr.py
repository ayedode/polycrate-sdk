from typing import Literal

ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_CATALOGUE_APPS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_catalogue_apps_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
