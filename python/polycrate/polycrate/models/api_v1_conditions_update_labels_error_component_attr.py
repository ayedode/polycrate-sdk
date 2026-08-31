from typing import Literal

ApiV1ConditionsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CONDITIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_conditions_update_labels_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateLabelsErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
