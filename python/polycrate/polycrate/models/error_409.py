from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_code_409_enum import ErrorCode409Enum, check_error_code_409_enum

T = TypeVar("T", bound="Error409")


@_attrs_define
class Error409:
    """
    Attributes:
        code (ErrorCode409Enum): * `conflict` - Conflict
            * `action_run_already_running` - Action Run Already Running
        detail (str):
        attr (None | str):
    """

    code: ErrorCode409Enum
    detail: str
    attr: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: str = self.code

        detail = self.detail

        attr: None | str
        attr = self.attr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "detail": detail,
                "attr": attr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = check_error_code_409_enum(d.pop("code"))

        detail = d.pop("detail")

        def _parse_attr(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        attr = _parse_attr(d.pop("attr"))

        error_409 = cls(
            code=code,
            detail=detail,
            attr=attr,
        )

        error_409.additional_properties = d
        return error_409

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
