from typing import Literal

ApiV1ContactsUpdateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null", "required"]

API_V1_CONTACTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsUpdateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_contacts_update_organization_id_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
