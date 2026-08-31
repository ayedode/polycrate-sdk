from typing import Literal

ApiV1PopsCreateNameErrorComponentAttr = Literal["name"]

API_V1_POPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pops_create_name_error_component_attr(value: str) -> ApiV1PopsCreateNameErrorComponentAttr:
    if value in API_V1_POPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
