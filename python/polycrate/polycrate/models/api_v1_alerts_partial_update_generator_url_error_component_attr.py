from typing import Literal

ApiV1AlertsPartialUpdateGeneratorUrlErrorComponentAttr = Literal["generator_url"]

API_V1_ALERTS_PARTIAL_UPDATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateGeneratorUrlErrorComponentAttr
] = {
    "generator_url",
}


def check_api_v1_alerts_partial_update_generator_url_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateGeneratorUrlErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
