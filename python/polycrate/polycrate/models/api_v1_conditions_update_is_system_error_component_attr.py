from typing import Literal

ApiV1ConditionsUpdateIsSystemErrorComponentAttr = Literal["is_system"]

API_V1_CONDITIONS_UPDATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsUpdateIsSystemErrorComponentAttr] = {
    "is_system",
}


def check_api_v1_conditions_update_is_system_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateIsSystemErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
