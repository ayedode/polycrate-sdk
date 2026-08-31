from typing import Literal

ApiV1CatalogueAppsArchiveCreateClaimErrorComponentAttr = Literal["claim"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateClaimErrorComponentAttr
] = {
    "claim",
}


def check_api_v1_catalogue_apps_archive_create_claim_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateClaimErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
