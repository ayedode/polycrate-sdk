from typing import Literal

ApiV1ConditionsPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CONDITIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_conditions_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
