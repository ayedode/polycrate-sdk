from typing import Literal

ApiV1IdpIdentityprovidersCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_idp_identityproviders_create_hostname_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateHostnameErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
