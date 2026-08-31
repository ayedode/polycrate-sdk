from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_idp_identityproviders_archive_create_hostname_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateHostnameErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
