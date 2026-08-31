from typing import Literal

ApiV1PrefixesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PREFIXES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_prefixes_create_labels_error_component_code(value: str) -> ApiV1PrefixesCreateLabelsErrorComponentCode:
    if value in API_V1_PREFIXES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
