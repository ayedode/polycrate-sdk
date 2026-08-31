from typing import Literal

ApiV1IdpIdentityprovidersListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_idp_identityproviders_list_state_not_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersListStateNotErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
