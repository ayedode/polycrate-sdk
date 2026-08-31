from typing import Literal

ApiV1PersonalNotesMinePartialUpdateContentErrorComponentAttr = Literal["content"]

API_V1_PERSONAL_NOTES_MINE_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PersonalNotesMinePartialUpdateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_personal_notes_mine_partial_update_content_error_component_attr(
    value: str,
) -> ApiV1PersonalNotesMinePartialUpdateContentErrorComponentAttr:
    if value in API_V1_PERSONAL_NOTES_MINE_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PERSONAL_NOTES_MINE_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
