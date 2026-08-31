from typing import Literal

ApiV1IdpIdentityprovidersListStateErrorComponentAttr = Literal["state"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_idp_identityproviders_list_state_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListStateErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
