from typing import Literal

ApiV1OrganizationsChoicesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_NOT_VALUES: set[ApiV1OrganizationsChoicesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_organizations_choices_list_state_not(value: str) -> ApiV1OrganizationsChoicesListStateNot:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_STATE_NOT_VALUES!r}"
    )
