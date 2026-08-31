from typing import Literal

ApiV1PoliciesCreateNameErrorComponentAttr = Literal["name"]

API_V1_POLICIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_policies_create_name_error_component_attr(value: str) -> ApiV1PoliciesCreateNameErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
