from typing import Literal

ApiV1ConditionsPartialUpdateIsSystemErrorComponentAttr = Literal["is_system"]

API_V1_CONDITIONS_PARTIAL_UPDATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateIsSystemErrorComponentAttr
] = {
    "is_system",
}


def check_api_v1_conditions_partial_update_is_system_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateIsSystemErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
