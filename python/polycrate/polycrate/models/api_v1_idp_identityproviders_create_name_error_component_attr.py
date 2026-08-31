from typing import Literal

ApiV1IdpIdentityprovidersCreateNameErrorComponentAttr = Literal["name"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_idp_identityproviders_create_name_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateNameErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
