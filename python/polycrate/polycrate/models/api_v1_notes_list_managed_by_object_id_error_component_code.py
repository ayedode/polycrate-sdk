from typing import Literal

ApiV1NotesListManagedByObjectIdErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_NOTES_LIST_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesListManagedByObjectIdErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_notes_list_managed_by_object_id_error_component_code(
    value: str,
) -> ApiV1NotesListManagedByObjectIdErrorComponentCode:
    if value in API_V1_NOTES_LIST_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
