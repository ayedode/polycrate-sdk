from typing import Literal

ApiV1ProvidersUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PROVIDERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_providers_update_labels_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateLabelsErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
