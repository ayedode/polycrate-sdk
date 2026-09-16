from typing import Literal

ApiV1CatalogueAppsPartialUpdateMaintainerIdErrorComponentAttr = Literal["maintainer_id"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MAINTAINER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateMaintainerIdErrorComponentAttr
] = {
    "maintainer_id",
}


def check_api_v1_catalogue_apps_partial_update_maintainer_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateMaintainerIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MAINTAINER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MAINTAINER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
