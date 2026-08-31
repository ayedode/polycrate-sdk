from typing import Literal

ApiV1AdminUsersCreateIsMaintenanceContactErrorComponentAttr = Literal["is_maintenance_contact"]

API_V1_ADMIN_USERS_CREATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersCreateIsMaintenanceContactErrorComponentAttr
] = {
    "is_maintenance_contact",
}


def check_api_v1_admin_users_create_is_maintenance_contact_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateIsMaintenanceContactErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
