from typing import Literal

ApiV1SecretmanagerManagersCreateKindErrorComponentAttr = Literal["kind"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_secretmanager_managers_create_kind_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateKindErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
