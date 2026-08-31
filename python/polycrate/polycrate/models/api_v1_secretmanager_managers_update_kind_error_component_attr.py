from typing import Literal

ApiV1SecretmanagerManagersUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_secretmanager_managers_update_kind_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateKindErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
