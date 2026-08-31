from typing import Literal

ApiV1CatalogueAppsUpdateClaimErrorComponentAttr = Literal["claim"]

API_V1_CATALOGUE_APPS_UPDATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsUpdateClaimErrorComponentAttr] = {
    "claim",
}


def check_api_v1_catalogue_apps_update_claim_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateClaimErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
