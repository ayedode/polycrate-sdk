from typing import Literal

ApiV1ContactsUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_CONTACTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_contacts_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1ContactsUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
