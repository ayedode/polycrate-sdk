from typing import Literal

ApiV1PrefixesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PREFIXES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_prefixes_update_labels_error_component_code(value: str) -> ApiV1PrefixesUpdateLabelsErrorComponentCode:
    if value in API_V1_PREFIXES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
