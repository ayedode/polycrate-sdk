from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_idp_identityproviders_partial_update_hostname_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
