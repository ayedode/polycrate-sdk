from typing import Literal

ApiV1IdpIdentityprovidersListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_VALUES: set[ApiV1IdpIdentityprovidersListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_idp_identityproviders_list_state(value: str) -> ApiV1IdpIdentityprovidersListState:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_STATE_VALUES!r}")
