from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_config_update_errors_errors import SystemConfigUpdateErrorsErrors


T = TypeVar("T", bound="SystemConfigUpdateErrors")


@_attrs_define
class SystemConfigUpdateErrors:
    """
    Attributes:
        error (str | Unset):
        errors (SystemConfigUpdateErrorsErrors | Unset):
    """

    error: str | Unset = UNSET
    errors: SystemConfigUpdateErrorsErrors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_config_update_errors_errors import SystemConfigUpdateErrorsErrors  # noqa: PLC0415

        d = dict(src_dict)
        error = d.pop("error", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: SystemConfigUpdateErrorsErrors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = SystemConfigUpdateErrorsErrors.from_dict(_errors)

        system_config_update_errors = cls(
            error=error,
            errors=errors,
        )

        system_config_update_errors.additional_properties = d
        return system_config_update_errors

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
