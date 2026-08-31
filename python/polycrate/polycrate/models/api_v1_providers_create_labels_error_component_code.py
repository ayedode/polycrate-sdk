from typing import Literal

ApiV1ProvidersCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PROVIDERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_providers_create_labels_error_component_code(
    value: str,
) -> ApiV1ProvidersCreateLabelsErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
