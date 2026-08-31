from typing import Literal

ApiV1DowntimesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOWNTIMES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_downtimes_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DowntimesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
