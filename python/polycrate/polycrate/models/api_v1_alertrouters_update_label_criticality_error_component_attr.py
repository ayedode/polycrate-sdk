from typing import Literal

ApiV1AlertroutersUpdateLabelCriticalityErrorComponentAttr = Literal["label_criticality"]

API_V1_ALERTROUTERS_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateLabelCriticalityErrorComponentAttr
] = {
    "label_criticality",
}


def check_api_v1_alertrouters_update_label_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateLabelCriticalityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
