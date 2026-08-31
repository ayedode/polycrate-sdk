from typing import Literal

ApiV1NotesCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_NOTES_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_notes_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1NotesCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
