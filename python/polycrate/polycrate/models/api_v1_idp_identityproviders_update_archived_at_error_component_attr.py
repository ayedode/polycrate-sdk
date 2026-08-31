from typing import Literal

ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_idp_identityproviders_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
