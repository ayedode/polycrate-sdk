from typing import Literal

ApiV1DowntimesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_downtimes_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DowntimesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
