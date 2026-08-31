from typing import Literal

ApiV1NotesListManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_NOTES_LIST_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesListManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_notes_list_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1NotesListManagedByObjectIdErrorComponentAttr:
    if value in API_V1_NOTES_LIST_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
