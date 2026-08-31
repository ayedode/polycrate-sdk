from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GrafanaDashboardRevision")


@_attrs_define
class GrafanaDashboardRevision:
    """
    Attributes:
        id (int):
        revision_number (int): Monotonically increasing revision counter per dashboard (1, 2, 3, …).
        source_version (int | None): Grafana-internal version number (meta.version).
        sync_checksum (str): SHA-256 of json.dumps(dashboard_json['dashboard'], sort_keys=True).
        imported_at (datetime.datetime):
        imported_by_task (str): Celery task ID or run marker for traceability.
        is_latest (bool):
    """

    id: int
    revision_number: int
    source_version: int | None
    sync_checksum: str
    imported_at: datetime.datetime
    imported_by_task: str
    is_latest: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        revision_number = self.revision_number

        source_version: int | None
        source_version = self.source_version

        sync_checksum = self.sync_checksum

        imported_at = self.imported_at.isoformat()

        imported_by_task = self.imported_by_task

        is_latest = self.is_latest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "revision_number": revision_number,
                "source_version": source_version,
                "sync_checksum": sync_checksum,
                "imported_at": imported_at,
                "imported_by_task": imported_by_task,
                "is_latest": is_latest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        revision_number = d.pop("revision_number")

        def _parse_source_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        source_version = _parse_source_version(d.pop("source_version"))

        sync_checksum = d.pop("sync_checksum")

        imported_at = datetime.datetime.fromisoformat(d.pop("imported_at"))

        imported_by_task = d.pop("imported_by_task")

        is_latest = d.pop("is_latest")

        grafana_dashboard_revision = cls(
            id=id,
            revision_number=revision_number,
            source_version=source_version,
            sync_checksum=sync_checksum,
            imported_at=imported_at,
            imported_by_task=imported_by_task,
            is_latest=is_latest,
        )

        grafana_dashboard_revision.additional_properties = d
        return grafana_dashboard_revision

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
