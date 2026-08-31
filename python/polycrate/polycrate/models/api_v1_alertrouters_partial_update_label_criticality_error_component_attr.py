from typing import Literal

ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponentAttr = Literal["label_criticality"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponentAttr
] = {
    "label_criticality",
}


def check_api_v1_alertrouters_partial_update_label_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
