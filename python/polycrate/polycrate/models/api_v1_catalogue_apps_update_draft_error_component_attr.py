from typing import Literal

ApiV1CatalogueAppsUpdateDraftErrorComponentAttr = Literal["draft"]

API_V1_CATALOGUE_APPS_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsUpdateDraftErrorComponentAttr] = {
    "draft",
}


def check_api_v1_catalogue_apps_update_draft_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateDraftErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
