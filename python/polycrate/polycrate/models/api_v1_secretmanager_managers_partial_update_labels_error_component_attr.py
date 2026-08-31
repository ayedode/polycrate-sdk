from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_secretmanager_managers_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
