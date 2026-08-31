from typing import Literal

ApiV1SecretmanagerManagersListKindErrorComponentAttr = Literal["kind"]

API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_secretmanager_managers_list_kind_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersListKindErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
