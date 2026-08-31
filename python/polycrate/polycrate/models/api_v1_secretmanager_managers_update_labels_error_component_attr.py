from typing import Literal

ApiV1SecretmanagerManagersUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_secretmanager_managers_update_labels_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateLabelsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
