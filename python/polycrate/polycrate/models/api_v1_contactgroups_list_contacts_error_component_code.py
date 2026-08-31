from typing import Literal

ApiV1ContactgroupsListContactsErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_CONTACTGROUPS_LIST_CONTACTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactgroupsListContactsErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_contactgroups_list_contacts_error_component_code(
    value: str,
) -> ApiV1ContactgroupsListContactsErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_LIST_CONTACTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_CONTACTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
