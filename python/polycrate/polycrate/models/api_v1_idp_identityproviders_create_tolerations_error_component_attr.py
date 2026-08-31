from typing import Literal

ApiV1IdpIdentityprovidersCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_idp_identityproviders_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateTolerationsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
