from typing import Literal

ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_catalogue_apps_partial_update_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
