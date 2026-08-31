from typing import Literal

ApiV1AdminUsersListRole = Literal["admin", "billing", "developer", "owner", "viewer"]

API_V1_ADMIN_USERS_LIST_ROLE_VALUES: set[ApiV1AdminUsersListRole] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_api_v1_admin_users_list_role(value: str) -> ApiV1AdminUsersListRole:
    if value in API_V1_ADMIN_USERS_LIST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_LIST_ROLE_VALUES!r}")
