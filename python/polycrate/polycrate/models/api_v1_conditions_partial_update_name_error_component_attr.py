from typing import Literal

ApiV1ConditionsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_CONDITIONS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_conditions_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
