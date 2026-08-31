from typing import Literal

ApiV1CatalogueAppsCreateDraftErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_CREATE_DRAFT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CatalogueAppsCreateDraftErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_create_draft_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateDraftErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_DRAFT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_DRAFT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
