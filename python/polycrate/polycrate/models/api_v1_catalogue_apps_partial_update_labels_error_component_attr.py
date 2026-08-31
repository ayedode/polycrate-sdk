from typing import Literal

ApiV1CatalogueAppsPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_catalogue_apps_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
