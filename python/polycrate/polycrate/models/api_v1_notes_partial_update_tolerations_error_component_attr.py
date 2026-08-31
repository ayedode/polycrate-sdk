from typing import Literal

ApiV1NotesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_NOTES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_notes_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
