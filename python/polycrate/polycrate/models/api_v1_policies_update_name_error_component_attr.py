from typing import Literal

ApiV1PoliciesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_POLICIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_policies_update_name_error_component_attr(value: str) -> ApiV1PoliciesUpdateNameErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
