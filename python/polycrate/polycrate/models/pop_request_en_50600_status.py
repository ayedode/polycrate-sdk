from typing import Literal

PopRequestEn50600Status = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_EN_50600_STATUS_VALUES: set[PopRequestEn50600Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_en_50600_status(value: str) -> PopRequestEn50600Status:
    if value in POP_REQUEST_EN_50600_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_EN_50600_STATUS_VALUES!r}")
