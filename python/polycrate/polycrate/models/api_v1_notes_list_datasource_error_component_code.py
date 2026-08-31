from typing import Literal

ApiV1NotesListDatasourceErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_NOTES_LIST_DATASOURCE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesListDatasourceErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_notes_list_datasource_error_component_code(value: str) -> ApiV1NotesListDatasourceErrorComponentCode:
    if value in API_V1_NOTES_LIST_DATASOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_DATASOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
