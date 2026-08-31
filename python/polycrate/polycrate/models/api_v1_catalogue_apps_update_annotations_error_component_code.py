from typing import Literal

ApiV1CatalogueAppsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CATALOGUE_APPS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_catalogue_apps_update_annotations_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
