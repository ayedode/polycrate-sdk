from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_secretmanager_managers_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
