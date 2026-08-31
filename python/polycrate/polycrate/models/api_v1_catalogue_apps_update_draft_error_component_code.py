from typing import Literal

ApiV1CatalogueAppsUpdateDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CatalogueAppsUpdateDraftErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_update_draft_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateDraftErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
