from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.note_kind_enum import NoteKindEnum, check_note_kind_enum

if TYPE_CHECKING:
    from ..models.note_simple_created_by_user_type_0 import NoteSimpleCreatedByUserType0
    from ..models.note_simple_project_type_0 import NoteSimpleProjectType0


T = TypeVar("T", bound="NoteSimple")


@_attrs_define
class NoteSimple:
    """Simple serializer for embedding Note in other serializers.

    Attributes:
        id (UUID):
        display_name (str): Human-readable name for the note
        name (str):
        kind (NoteKindEnum): * `info` - Information
            * `warning` - Warning
            * `todo` - Todo
            * `reminder` - Reminder
            * `comment` - Comment
            * `post-mortem` - Post-Mortem
            * `provider-status` - Provider Status
            * `news` - News
            * `object-note` - Object Note
            * `meeting` - Meeting
            * `restore-test` - Restore Test
            * `app-release` - App Release
        reconciliation_running (bool):
        url (str):
        total_time_tracked_hours (None | str):
        created_by_user (None | NoteSimpleCreatedByUserType0):
        project (None | NoteSimpleProjectType0):
    """

    id: UUID
    display_name: str
    name: str
    kind: NoteKindEnum
    reconciliation_running: bool
    url: str
    total_time_tracked_hours: None | str
    created_by_user: None | NoteSimpleCreatedByUserType0
    project: None | NoteSimpleProjectType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.note_simple_created_by_user_type_0 import NoteSimpleCreatedByUserType0
        from ..models.note_simple_project_type_0 import NoteSimpleProjectType0

        id = str(self.id)

        display_name = self.display_name

        name = self.name

        kind: str = self.kind

        reconciliation_running = self.reconciliation_running

        url = self.url

        total_time_tracked_hours: None | str
        total_time_tracked_hours = self.total_time_tracked_hours

        created_by_user: dict[str, Any] | None
        if isinstance(self.created_by_user, NoteSimpleCreatedByUserType0):
            created_by_user = self.created_by_user.to_dict()
        else:
            created_by_user = self.created_by_user

        project: dict[str, Any] | None
        if isinstance(self.project, NoteSimpleProjectType0):
            project = self.project.to_dict()
        else:
            project = self.project

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "name": name,
                "kind": kind,
                "reconciliation_running": reconciliation_running,
                "url": url,
                "total_time_tracked_hours": total_time_tracked_hours,
                "created_by_user": created_by_user,
                "project": project,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_simple_created_by_user_type_0 import NoteSimpleCreatedByUserType0
        from ..models.note_simple_project_type_0 import NoteSimpleProjectType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        display_name = d.pop("display_name")

        name = d.pop("name")

        kind = check_note_kind_enum(d.pop("kind"))

        reconciliation_running = d.pop("reconciliation_running")

        url = d.pop("url")

        def _parse_total_time_tracked_hours(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        total_time_tracked_hours = _parse_total_time_tracked_hours(d.pop("total_time_tracked_hours"))

        def _parse_created_by_user(data: object) -> None | NoteSimpleCreatedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_user_type_0 = NoteSimpleCreatedByUserType0.from_dict(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NoteSimpleCreatedByUserType0, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user"))

        def _parse_project(data: object) -> None | NoteSimpleProjectType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                project_type_0 = NoteSimpleProjectType0.from_dict(data)

                return project_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NoteSimpleProjectType0, data)

        project = _parse_project(d.pop("project"))

        note_simple = cls(
            id=id,
            display_name=display_name,
            name=name,
            kind=kind,
            reconciliation_running=reconciliation_running,
            url=url,
            total_time_tracked_hours=total_time_tracked_hours,
            created_by_user=created_by_user,
            project=project,
        )

        note_simple.additional_properties = d
        return note_simple

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
