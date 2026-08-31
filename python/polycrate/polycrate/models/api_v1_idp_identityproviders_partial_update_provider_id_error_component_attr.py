from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_idp_identityproviders_partial_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
