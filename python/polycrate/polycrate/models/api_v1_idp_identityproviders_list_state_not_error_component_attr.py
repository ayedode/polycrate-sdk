from typing import Literal

ApiV1IdpIdentityprovidersListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_idp_identityproviders_list_state_not_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListStateNotErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
