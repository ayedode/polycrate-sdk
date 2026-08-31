from typing import Literal

ApiV1ConditionsCreateIsSystemErrorComponentAttr = Literal["is_system"]

API_V1_CONDITIONS_CREATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsCreateIsSystemErrorComponentAttr] = {
    "is_system",
}


def check_api_v1_conditions_create_is_system_error_component_attr(
    value: str,
) -> ApiV1ConditionsCreateIsSystemErrorComponentAttr:
    if value in API_V1_CONDITIONS_CREATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_IS_SYSTEM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
