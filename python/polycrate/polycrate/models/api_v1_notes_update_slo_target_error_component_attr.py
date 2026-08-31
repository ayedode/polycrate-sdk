from typing import Literal

ApiV1NotesUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_NOTES_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateSloTargetErrorComponentAttr] = {
    "slo_target",
}


def check_api_v1_notes_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateSloTargetErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
