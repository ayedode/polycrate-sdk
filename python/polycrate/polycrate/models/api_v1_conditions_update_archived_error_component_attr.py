from typing import Literal

ApiV1ConditionsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CONDITIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_conditions_update_archived_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateArchivedErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
