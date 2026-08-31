from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_idp_identityproviders_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
