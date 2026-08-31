from typing import Literal

ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_CATALOGUE_APPS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_catalogue_apps_update_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
