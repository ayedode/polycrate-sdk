from typing import Literal

ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_idp_identityproviders_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
