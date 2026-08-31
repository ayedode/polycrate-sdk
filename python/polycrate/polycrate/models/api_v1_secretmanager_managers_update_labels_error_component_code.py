from typing import Literal

ApiV1SecretmanagerManagersUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_secretmanager_managers_update_labels_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateLabelsErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
