from typing import Literal

ApiV1ContactgroupsListContactsErrorComponentAttr = Literal["contacts"]

API_V1_CONTACTGROUPS_LIST_CONTACTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsListContactsErrorComponentAttr
] = {
    "contacts",
}


def check_api_v1_contactgroups_list_contacts_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsListContactsErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_LIST_CONTACTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_CONTACTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
