from typing import Literal

ApiV1ConditionsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CONDITIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_conditions_create_kind_error_component_attr(value: str) -> ApiV1ConditionsCreateKindErrorComponentAttr:
    if value in API_V1_CONDITIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
