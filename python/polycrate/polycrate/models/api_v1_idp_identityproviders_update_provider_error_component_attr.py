from typing import Literal

ApiV1IdpIdentityprovidersUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_idp_identityproviders_update_provider_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateProviderErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
