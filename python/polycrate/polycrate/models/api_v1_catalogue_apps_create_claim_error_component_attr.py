from typing import Literal

ApiV1CatalogueAppsCreateClaimErrorComponentAttr = Literal["claim"]

API_V1_CATALOGUE_APPS_CREATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CatalogueAppsCreateClaimErrorComponentAttr] = {
    "claim",
}


def check_api_v1_catalogue_apps_create_claim_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateClaimErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_CLAIM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
