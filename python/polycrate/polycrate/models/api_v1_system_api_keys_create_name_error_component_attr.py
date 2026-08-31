from typing import Literal

ApiV1SystemApiKeysCreateNameErrorComponentAttr = Literal["name"]

API_V1_SYSTEM_API_KEYS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1SystemApiKeysCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_system_api_keys_create_name_error_component_attr(
    value: str,
) -> ApiV1SystemApiKeysCreateNameErrorComponentAttr:
    if value in API_V1_SYSTEM_API_KEYS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SYSTEM_API_KEYS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
