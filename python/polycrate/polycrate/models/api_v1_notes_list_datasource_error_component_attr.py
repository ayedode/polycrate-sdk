from typing import Literal

ApiV1NotesListDatasourceErrorComponentAttr = Literal["datasource"]

API_V1_NOTES_LIST_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListDatasourceErrorComponentAttr] = {
    "datasource",
}


def check_api_v1_notes_list_datasource_error_component_attr(value: str) -> ApiV1NotesListDatasourceErrorComponentAttr:
    if value in API_V1_NOTES_LIST_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
