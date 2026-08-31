from typing import Literal

ApiV1CatalogueAppsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CATALOGUE_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_catalogue_apps_create_labels_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateLabelsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
