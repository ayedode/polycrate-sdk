from typing import Literal

ApiV1ContactsPartialUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_CONTACTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_contacts_partial_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
