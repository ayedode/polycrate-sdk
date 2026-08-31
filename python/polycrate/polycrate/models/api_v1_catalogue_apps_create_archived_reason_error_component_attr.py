from typing import Literal

ApiV1CatalogueAppsCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_CATALOGUE_APPS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_catalogue_apps_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
