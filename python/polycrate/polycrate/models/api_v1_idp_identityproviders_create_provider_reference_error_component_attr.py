from typing import Literal

ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_idp_identityproviders_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
