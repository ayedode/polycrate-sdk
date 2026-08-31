from typing import Literal

ApiV1UsersPartialUpdateIsMaintenanceContactErrorComponentAttr = Literal["is_maintenance_contact"]

API_V1_USERS_PARTIAL_UPDATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1UsersPartialUpdateIsMaintenanceContactErrorComponentAttr
] = {
    "is_maintenance_contact",
}


def check_api_v1_users_partial_update_is_maintenance_contact_error_component_attr(
    value: str,
) -> ApiV1UsersPartialUpdateIsMaintenanceContactErrorComponentAttr:
    if value in API_V1_USERS_PARTIAL_UPDATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_PARTIAL_UPDATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
