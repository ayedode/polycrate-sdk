from typing import Literal

ApiV1ContactsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_CONTACTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_contacts_update_kind_error_component_attr(value: str) -> ApiV1ContactsUpdateKindErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
