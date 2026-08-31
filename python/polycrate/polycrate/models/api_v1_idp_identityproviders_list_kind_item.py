from typing import Literal

ApiV1IdpIdentityprovidersListKindItem = Literal["authentik", "generic", "keycloak"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_KIND_ITEM_VALUES: set[ApiV1IdpIdentityprovidersListKindItem] = {
    "authentik",
    "generic",
    "keycloak",
}


def check_api_v1_idp_identityproviders_list_kind_item(value: str) -> ApiV1IdpIdentityprovidersListKindItem:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_KIND_ITEM_VALUES!r}"
    )
