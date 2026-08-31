from typing import Literal

ApiV1IdpIdentityprovidersListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_VALUES: set[ApiV1IdpIdentityprovidersListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_idp_identityproviders_list_state_not(value: str) -> ApiV1IdpIdentityprovidersListStateNot:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_NOT_VALUES!r}"
    )
