from typing import Literal

ApiV1NotesUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_NOTES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_notes_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
