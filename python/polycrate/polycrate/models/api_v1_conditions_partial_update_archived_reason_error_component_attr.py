from typing import Literal

ApiV1ConditionsPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_CONDITIONS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_conditions_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
