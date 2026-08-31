from typing import Literal

ApiV1CatalogueAppsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_catalogue_apps_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
