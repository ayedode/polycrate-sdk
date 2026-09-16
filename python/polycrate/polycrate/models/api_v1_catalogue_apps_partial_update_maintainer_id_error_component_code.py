from typing import Literal

ApiV1CatalogueAppsPartialUpdateMaintainerIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MAINTAINER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateMaintainerIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_catalogue_apps_partial_update_maintainer_id_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateMaintainerIdErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MAINTAINER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MAINTAINER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
