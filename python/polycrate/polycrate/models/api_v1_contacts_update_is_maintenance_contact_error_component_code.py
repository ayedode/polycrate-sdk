from typing import Literal

ApiV1ContactsUpdateIsMaintenanceContactErrorComponentCode = Literal["invalid", "null"]

API_V1_CONTACTS_UPDATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsUpdateIsMaintenanceContactErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_contacts_update_is_maintenance_contact_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateIsMaintenanceContactErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
