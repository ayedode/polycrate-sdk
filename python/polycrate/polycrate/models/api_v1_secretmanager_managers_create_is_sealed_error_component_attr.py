from typing import Literal

ApiV1SecretmanagerManagersCreateIsSealedErrorComponentAttr = Literal["is_sealed"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_IS_SEALED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateIsSealedErrorComponentAttr
] = {
    "is_sealed",
}


def check_api_v1_secretmanager_managers_create_is_sealed_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateIsSealedErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_IS_SEALED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_IS_SEALED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
