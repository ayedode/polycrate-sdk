from typing import Literal

ApiV1ConditionsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_CONDITIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_conditions_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
