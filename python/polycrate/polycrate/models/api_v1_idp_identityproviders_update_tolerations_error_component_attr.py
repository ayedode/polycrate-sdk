from typing import Literal

ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_idp_identityproviders_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
