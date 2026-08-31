from typing import Literal

ApiV1IdpIdentityprovidersUpdateNameErrorComponentAttr = Literal["name"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_idp_identityproviders_update_name_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateNameErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
