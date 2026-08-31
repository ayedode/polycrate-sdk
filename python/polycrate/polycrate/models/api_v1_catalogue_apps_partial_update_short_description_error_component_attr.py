from typing import Literal

ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponentAttr = Literal["short_description"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponentAttr
] = {
    "short_description",
}


def check_api_v1_catalogue_apps_partial_update_short_description_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SHORT_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
