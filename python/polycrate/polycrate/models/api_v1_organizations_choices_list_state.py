from typing import Literal

ApiV1OrganizationsChoicesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_VALUES: set[ApiV1OrganizationsChoicesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_organizations_choices_list_state(value: str) -> ApiV1OrganizationsChoicesListState:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_VALUES!r}")
