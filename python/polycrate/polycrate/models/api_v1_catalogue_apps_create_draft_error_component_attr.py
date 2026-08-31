from typing import Literal

ApiV1CatalogueAppsCreateDraftErrorComponentAttr = Literal["draft"]

API_V1_CATALOGUE_APPS_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsCreateDraftErrorComponentAttr] = {
    "draft",
}


def check_api_v1_catalogue_apps_create_draft_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateDraftErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_DRAFT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
