from typing import Literal

ApiV1ProvidersPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PROVIDERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_providers_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
