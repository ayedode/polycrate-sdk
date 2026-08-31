from typing import Literal

ApiV1CatalogueAppsUpdateCreatedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CATALOGUE_APPS_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsUpdateCreatedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_catalogue_apps_update_created_by_user_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateCreatedByUserErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
