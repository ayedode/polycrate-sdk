from typing import Literal

ApiV1OrganizationsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ORGANIZATIONS_LIST_STATE_VALUES: set[ApiV1OrganizationsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_organizations_list_state(value: str) -> ApiV1OrganizationsListState:
    if value in API_V1_ORGANIZATIONS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_STATE_VALUES!r}")
