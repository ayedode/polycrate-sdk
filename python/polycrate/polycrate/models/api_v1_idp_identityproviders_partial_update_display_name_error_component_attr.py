from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_idp_identityproviders_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
