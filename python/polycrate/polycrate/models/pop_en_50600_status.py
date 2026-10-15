from typing import Literal

PopEn50600Status = Literal["no", "planned", "unknown", "yes"]

POP_EN_50600_STATUS_VALUES: set[PopEn50600Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_en_50600_status(value: str) -> PopEn50600Status:
    if value in POP_EN_50600_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_EN_50600_STATUS_VALUES!r}")
