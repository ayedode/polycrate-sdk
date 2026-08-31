from typing import Literal

ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_catalogue_apps_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
