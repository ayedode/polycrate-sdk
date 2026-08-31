from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.cli_activity_update_request_status_enum import (
    CLIActivityUpdateRequestStatusEnum,
    check_cli_activity_update_request_status_enum,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCLIActivityUpdateRequestRequest")


@_attrs_define
class PatchedCLIActivityUpdateRequestRequest:
    """
    Attributes:
        exit_code (int | Unset):
        finished_at (datetime.datetime | Unset):
        duration_seconds (float | Unset):
        status (CLIActivityUpdateRequestStatusEnum | Unset): * `success` - success
            * `failed` - failed
    """

    exit_code: int | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    duration_seconds: float | Unset = UNSET
    status: CLIActivityUpdateRequestStatusEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exit_code = self.exit_code

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        duration_seconds = self.duration_seconds

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.exit_code, Unset):
            files.append(("exit_code", (None, str(self.exit_code).encode(), "text/plain")))

        if not isinstance(self.finished_at, Unset):
            files.append(("finished_at", (None, self.finished_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.duration_seconds, Unset):
            files.append(("duration_seconds", (None, str(self.duration_seconds).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exit_code = d.pop("exit_code", UNSET)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)

        duration_seconds = d.pop("duration_seconds", UNSET)

        _status = d.pop("status", UNSET)
        status: CLIActivityUpdateRequestStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_cli_activity_update_request_status_enum(_status)

        patched_cli_activity_update_request_request = cls(
            exit_code=exit_code,
            finished_at=finished_at,
            duration_seconds=duration_seconds,
            status=status,
        )

        patched_cli_activity_update_request_request.additional_properties = d
        return patched_cli_activity_update_request_request

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
