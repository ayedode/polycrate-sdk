from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponentAttr = Literal["is_sealed"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_IS_SEALED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponentAttr
] = {
    "is_sealed",
}


def check_api_v1_secretmanager_managers_partial_update_is_sealed_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_IS_SEALED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_IS_SEALED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
