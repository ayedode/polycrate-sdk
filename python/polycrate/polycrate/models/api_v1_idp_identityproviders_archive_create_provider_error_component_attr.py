from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_idp_identityproviders_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
