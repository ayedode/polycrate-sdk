from typing import Literal

ApiV1CatalogueAppsPartialUpdateDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateDraftErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_partial_update_draft_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateDraftErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
