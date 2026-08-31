from typing import Literal

ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponentAttr = Literal["is_maintenance_contact"]

API_V1_CONTACTS_ARCHIVE_CREATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponentAttr
] = {
    "is_maintenance_contact",
}


def check_api_v1_contacts_archive_create_is_maintenance_contact_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_IS_MAINTENANCE_CONTACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
