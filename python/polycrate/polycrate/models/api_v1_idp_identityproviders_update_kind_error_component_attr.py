from typing import Literal

ApiV1IdpIdentityprovidersUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_idp_identityproviders_update_kind_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateKindErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
