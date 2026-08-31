from typing import Literal

ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_idp_identityproviders_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
