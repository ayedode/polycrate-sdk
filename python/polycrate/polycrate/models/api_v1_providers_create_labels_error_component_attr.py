from typing import Literal

ApiV1ProvidersCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PROVIDERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_providers_create_labels_error_component_attr(
    value: str,
) -> ApiV1ProvidersCreateLabelsErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
